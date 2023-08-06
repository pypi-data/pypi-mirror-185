import click
import functools

import smaug.models.stanza
from smaug import models
from smaug import random
from smaug import transform
from smaug import ops
from smaug.ops import lang_model
from smaug.ops import text_generation
from smaug.cli import accelerator
from smaug.cli import fmt
from smaug.cli import processor
from smaug.cli import validation


_SWAP_NUM_CMD = "transf-swp-num"
_SWAP_NE_CMD = "transf-swp-ne"
_SWAP_POISSON_SPAN_CMD = "transf-swp-poisson-span"
_NEG_CMD = "transf-neg"
_DEL_PUNCT_SPAN_CMD = "transf-del-punct-span"
_INS_TEXT_CMD = "transf-ins-text"


@click.command(_SWAP_NUM_CMD, short_help="Swap a number for text with regex and mT5.")
@click.option(
    "--batch-size",
    default=16,
    show_default=True,
    help="Batch size when processing records.",
)
@click.option("--no-gpu", is_flag=True, help="Disable gpu.")
@processor.make
@processor.post_run(validation.rm_eq, cli_transforms=[_SWAP_NUM_CMD])
@processor.post_run(
    validation.rm_pattern, pattern=r"<extra_id_\d{1,2}>", cli_transforms=[_SWAP_NUM_CMD]
)
@processor.post_run(
    validation.keep_leq_char_ins,
    chars="<>()[]{}_",
    max_insertions=0,
    cli_transforms=[_SWAP_NUM_CMD],
)
@processor.post_run(validation.keep_eq_num_count, cli_transforms=[_SWAP_NUM_CMD])
@click.pass_context
def swap_num(ctx, datasets, batch_size, no_gpu):
    """Swaps a number for text using regex and mT5.

    This operation is a transformation.
    It searches for numbers in the original records using regular expressions and
    then uses Google's mT5 to replace the one of the found expressions with text.

    The generated sentences are not guarantied to have a new number replacing the
    old one, as the model is free to generate any text.

    It is possible to have other validations to better ensure these conditions
    are met.
    """
    total_records = sum(len(datasets["records"]) for datasets in datasets)
    if total_records == 0:
        click.echo(fmt.no_records_message("Swap a Number for Text"))
        return datasets

    ctx.obj.register_transform(_SWAP_NUM_CMD)

    gpu = accelerator.use_gpu(no_gpu)

    rng = random.numpy_seeded_rng()

    mask_func = functools.partial(
        ops.mask_detections,
        detect_func=ops.regex_detect_numbers,
        mask_func=lang_model.mT5_masking_function,
        rng=rng,
        max_masks=1,
    )
    model, tokenizer = models.mT5_load()
    mT5_func = functools.partial(
        lang_model.mT5_generate, model=model, tokenizer=tokenizer, cuda=gpu
    )

    transf_func = functools.partial(
        transform.mask_and_fill,
        perturbation=_SWAP_NUM_CMD,
        mask_func=mask_func,
        fill_func=mT5_func,
    )

    processed = []

    pbar = fmt.pbar_from_total(total_records, "Swap a Number for Text")
    for dataset in datasets:
        old_records = dataset["records"]
        new_records = []

        for i in range(0, len(old_records), batch_size):
            batch = old_records[i : i + batch_size]
            records = transf_func(batch)
            new_records.extend(records)
            pbar.update(len(batch))

        dataset["records"] = new_records

        processed.append(dataset)
    return processed


@click.command(
    _SWAP_NE_CMD,
    short_help="Swap a named entity for text with named entity recognition and mT5.",
)
@click.option(
    "--batch-size",
    default=16,
    show_default=True,
    help="Batch size when processing records.",
)
@click.option("--no-gpu", is_flag=True, help="Disable gpu.")
@processor.make
@processor.post_run(validation.rm_eq, cli_transforms=[_SWAP_NE_CMD])
@processor.post_run(
    validation.rm_pattern, pattern=r"<extra_id_\d{1,2}>", cli_transforms=[_SWAP_NE_CMD]
)
@processor.post_run(
    validation.keep_leq_char_ins,
    chars="<>()[]{}_",
    max_insertions=0,
    cli_transforms=[_SWAP_NE_CMD],
)
@processor.post_run(validation.keep_eq_ne_count, cli_transforms=[_SWAP_NE_CMD])
@click.pass_context
def swap_ne(ctx, datasets, batch_size, no_gpu):
    """Swaps a single named entity for text using named entity recognition and mT5.

    This operation is a transformation.
    It searches for named entities in the original records using a stanza model and
    then uses Google's mT5 to replace one of the found expressions with text.

    The generated sentences are not guarantied to have a new named entity replacing the
    old one, as the model is free to generate any text.

    It is possible to have other validations to better ensure these conditions
    are met.
    """
    total_records = sum(
        len(dataset["records"])
        for dataset in datasets
        if smaug.models.stanza.stanza_ner_lang_available(dataset["lang"])
    )
    if total_records == 0:
        click.echo(fmt.no_records_message("Swap a Named Entitiy for Text"))
        return datasets

    ctx.obj.register_transform(_SWAP_NE_CMD)

    gpu = accelerator.use_gpu(no_gpu)
    rng = random.numpy_seeded_rng()

    model, tokenizer = models.mT5_load()
    mT5_func = functools.partial(
        lang_model.mT5_generate, model=model, tokenizer=tokenizer, cuda=gpu
    )

    processed = []

    pbar = fmt.pbar_from_total(total_records, "Swap a Named Entitiy for Text")
    for dataset in datasets:
        lang = dataset["lang"]
        if not smaug.models.stanza.stanza_ner_lang_available(lang):
            processed.append(dataset)
            continue
        ner_pipeline = models.stanza_ner_load(lang, gpu)
        ner_func = functools.partial(
            ops.stanza_detect_named_entities,
            ner_pipeline=ner_pipeline,
        )
        mask_func = functools.partial(
            ops.mask_detections,
            detect_func=ner_func,
            mask_func=lang_model.mT5_masking_function,
            rng=rng,
            max_masks=1,
        )

        transf_func = functools.partial(
            transform.mask_and_fill,
            perturbation=_SWAP_NE_CMD,
            mask_func=mask_func,
            fill_func=mT5_func,
        )

        old_records = dataset["records"]
        new_records = []

        for i in range(0, len(old_records), batch_size):
            batch = old_records[i : i + batch_size]
            records = transf_func(batch)
            new_records.extend(records)
            pbar.update(len(batch))

        dataset["records"] = new_records

        processed.append(dataset)
    return processed


@click.command(_NEG_CMD, short_help="Negate the sentence with polyjuice.")
@click.option(
    "--batch-size",
    default=16,
    show_default=True,
    help="Batch size when processing records.",
)
@click.option("--no-gpu", is_flag=True, help="Disable gpu.")
@processor.make
@processor.post_run(validation.rm_eq, cli_transforms=[_NEG_CMD])
@processor.post_run(validation.rm_pattern, pattern="EMPTY", cli_transforms=[_NEG_CMD])
@processor.post_run(validation.keep_contradiction, cli_transforms=[_NEG_CMD])
@click.pass_context
def negate(ctx, datasets, batch_size, no_gpu):
    """Negates the received sentences with polyjuice.

    This operation is a transformation.
    It tries to negate the sentence if possible.
    This transformation is only available for to-english datasets.
    """
    total_records = sum(
        len(orig["records"]) for orig in datasets if orig["lang"] == "en"
    )
    if total_records == 0:
        click.echo(fmt.no_records_message("Negate the Sentence"))
        return datasets

    ctx.obj.register_transform(_NEG_CMD)

    gpu = accelerator.use_gpu(no_gpu)

    rng = random.numpy_seeded_rng()
    pos_pipeline = models.stanza_pos_load("en", gpu)
    model, tokenizer = models.polyjuice_load()
    neg_polyjuice = functools.partial(
        text_generation.polyjuice_negate,
        pos_pipeline=pos_pipeline,
        model=model,
        tokenizer=tokenizer,
        rng=rng,
        cuda=gpu,
    )
    transf_func = functools.partial(
        transform.negate,
        perturbation=_NEG_CMD,
        polyjuice_func=neg_polyjuice,
    )

    pbar = fmt.pbar_from_total(total_records, "Negate the Sentence")

    processed = []
    for orig in datasets:
        if orig["lang"] == "en":
            old_records = orig["records"]
            new_records = []

            for i in range(0, len(old_records), batch_size):
                batch = old_records[i : i + batch_size]
                records = transf_func(batch)
                new_records.extend(records)
                pbar.update(len(batch))

            orig["records"] = new_records

        processed.append(orig)

    return processed


@click.command(
    _DEL_PUNCT_SPAN_CMD, short_help="Removes a span between two punctuation symbols."
)
@click.option(
    "--punct",
    "-p",
    default=",.!?",
    help="punctuation symbols to consider.",
    show_default=True,
)
@click.option(
    "--low",
    "-l",
    type=int,
    default=4,
    help="minimum number of words for a span to be eligible for deletion.",
    show_default=True,
)
@click.option(
    "--high",
    "-h",
    type=int,
    default=10,
    help="maximum number of words for a span to be eligible for deletion.",
    show_default=True,
)
@processor.make
@click.pass_context
def delete_punct_span(ctx, datasets, punct, low, high):
    """Removes a span between two punctuation symbols.

    This operation is a transformation.
    It detects the following symbols: ,.!? , and deletes a span between two of them.
    It also deletes the symbol to the right of the span.
    """
    total_records = sum(len(datasets["records"]) for datasets in datasets)
    if total_records == 0:
        click.echo(fmt.no_records_message(f"Delete a span between [{punct}]+ matches."))
        return datasets

    ctx.obj.register_transform(_DEL_PUNCT_SPAN_CMD)
    rng = random.numpy_seeded_rng()
    transf_func = functools.partial(
        transform.punct_span_delete,
        perturbation=_DEL_PUNCT_SPAN_CMD,
        rng=rng,
        punct=punct,
        low=low,
        high=high,
    )

    processed = []

    pbar = fmt.pbar_from_total(
        total_records, f"Delete a span between [{punct}]+ matches."
    )
    for dataset in datasets:
        old_records = dataset["records"]
        dataset["records"] = transf_func(old_records)

        pbar.update(len(old_records))

        processed.append(dataset)
    return processed


@click.command(_INS_TEXT_CMD, short_help="Insert random text with mT5.")
@click.option(
    "--prob",
    "-p",
    default=0.1,
    show_default=True,
    help="Probability of inserting a mask between two tokens",
)
@click.option(
    "--max-masks",
    default=3,
    show_default=True,
    help="Max masks to add for mT5 to fill.",
)
@click.option(
    "--batch-size",
    default=16,
    show_default=True,
    help="Batch size when processing records.",
)
@click.option("--no-gpu", is_flag=True, help="Disable gpu.")
@processor.make
@processor.post_run(validation.rm_eq, cli_transforms=[_INS_TEXT_CMD])
@processor.post_run(
    validation.rm_pattern, pattern=r"<extra_id_\d{1,2}>", cli_transforms=[_INS_TEXT_CMD]
)
@click.pass_context
def insert_text(ctx, datasets, prob, max_masks, batch_size, no_gpu):
    """Randomly inserts text using mT5.

    This operation is a transformation.
    It randomly adds masks between the words of the original sentence and
    takes as the output the sentence with the masks filled with mT5.
    """
    total_records = sum(len(datasets["records"]) for datasets in datasets)
    if total_records == 0:
        click.echo(fmt.no_records_message("Insert Text"))
        return datasets

    ctx.obj.register_transform(_INS_TEXT_CMD)

    gpu = accelerator.use_gpu(no_gpu)
    rng = random.numpy_seeded_rng()
    mask_func = functools.partial(
        ops.mask_random_insert,
        func=lang_model.mT5_masking_function,
        rng=rng,
        p=prob,
        max_masks=max_masks,
    )

    model, tokenizer = models.mT5_load()
    mT5_func = functools.partial(
        lang_model.mT5_generate, model=model, tokenizer=tokenizer, cuda=gpu
    )

    transf_func = functools.partial(
        transform.mask_and_fill,
        perturbation=_INS_TEXT_CMD,
        mask_func=mask_func,
        fill_func=mT5_func,
    )

    processed = []

    pbar = fmt.pbar_from_total(total_records, _INS_TEXT_CMD)
    for dataset in datasets:
        old_records = dataset["records"]
        new_records = []

        for i in range(0, len(old_records), batch_size):
            batch = old_records[i : i + batch_size]
            records = transf_func(batch)
            new_records.extend(records)
            pbar.update(len(batch))

        dataset["records"] = new_records

        processed.append(dataset)
    return processed


@click.command(
    _SWAP_POISSON_SPAN_CMD, short_help="Replace random spans of text with mT5."
)
@click.option(
    "--batch-size",
    default=16,
    show_default=True,
    help="Batch size when processing records.",
)
@click.option("--no-gpu", is_flag=True, help="Disable gpu.")
@processor.make
@processor.post_run(validation.rm_eq, cli_transforms=[_SWAP_POISSON_SPAN_CMD])
@processor.post_run(
    validation.rm_pattern,
    pattern=r"<extra_id_\d{1,2}>",
    cli_transforms=[_SWAP_POISSON_SPAN_CMD],
)
@click.pass_context
def swap_poisson_span(ctx, datasets, batch_size, no_gpu):
    """Randomly replaces text spans with sizes following a Poisson distribution.

    This operation is a transformation.
    It masks a span of text on the original sentence, where the number
    of masked words (can be 0) is given by the Poisson distribution, and
    takes as the output the sentence with the masks filled with mT5.
    """
    total_records = sum(len(datasets["records"]) for datasets in datasets)
    if total_records == 0:
        click.echo(fmt.no_records_message("Insert Text"))
        return datasets

    ctx.obj.register_transform(_SWAP_POISSON_SPAN_CMD)

    gpu = accelerator.use_gpu(no_gpu)
    rng = random.numpy_seeded_rng()
    mask_func = functools.partial(
        ops.mask_poisson_spans,
        func=lang_model.mT5_masking_function,
        rng=rng,
    )

    model, tokenizer = models.mT5_load()
    mT5_func = functools.partial(
        lang_model.mT5_generate, model=model, tokenizer=tokenizer, cuda=gpu
    )

    transf_func = functools.partial(
        transform.mask_and_fill,
        perturbation=_SWAP_POISSON_SPAN_CMD,
        mask_func=mask_func,
        fill_func=mT5_func,
    )

    processed = []

    pbar = fmt.pbar_from_total(total_records, _SWAP_POISSON_SPAN_CMD)
    for dataset in datasets:
        old_records = dataset["records"]
        new_records = []

        for i in range(0, len(old_records), batch_size):
            batch = old_records[i : i + batch_size]
            records = transf_func(batch)
            new_records.extend(records)
            pbar.update(len(batch))

        dataset["records"] = new_records

        processed.append(dataset)
    return processed
