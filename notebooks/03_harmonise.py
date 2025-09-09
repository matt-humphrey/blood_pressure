import marimo

__generated_with = "0.15.2"
app = marimo.App(width="medium")


@app.cell
def _():
    import re
    from dataclasses import asdict, dataclass, field
    from functools import partial
    from pathlib import Path
    from typing import Any

    import banksia as bk
    import marimo as mo
    import polars as pl
    import pyreadstat

    return bk, pl


@app.cell
def _():
    from blood_pressure import (
        DATA_TRANSFORMS,
        make_interim_datasets,
        transform_datasets,
    )
    from blood_pressure.config import DATASETS, INTERIM_DATA, METADATA, PROCESSED_DATA, RAW_DATA

    return (
        DATASETS,
        DATA_TRANSFORMS,
        INTERIM_DATA,
        METADATA,
        transform_datasets,
    )


@app.cell
def _():
    # make_interim_datasets(DATASETS)
    return


@app.cell
def _(DATASETS, INTERIM_DATA, bk):
    dfs, metas = {}, {}

    for name, dset in DATASETS.items():
        df, meta = bk.read_sav(INTERIM_DATA / dset["file"])
        dfs[name] = df
        metas[name] = meta
    return dfs, metas


@app.cell
def _(DATA_TRANSFORMS, METADATA, bk, dfs, metas, transform_datasets):
    transformed_dfs = transform_datasets(dfs, DATA_TRANSFORMS)
    transformed_metas = bk.transform_metadata(metas, METADATA)
    return transformed_dfs, transformed_metas


@app.cell
def _(pl, transformed_dfs):
    transformed_dfs["G208"].select(pl.col(r"^.*DM\d+.*$"))
    return


@app.cell
def _(pl, transformed_metas):
    transformed_metas["G208"].filter(pl.col("Variable").str.contains(r"DM3"))
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
