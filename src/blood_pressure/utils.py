from functools import reduce
from pathlib import Path
from typing import Callable, Literal, TypeAlias

import banksia as bk
import polars as pl
from polars import DataFrame

from blood_pressure.config import INTERIM_DATA, RAW_DATA

__all__ = [
    "apply_pipeline",
    "make_interim_datasets",
    "read_all_datasets",
    "transform_datasets",
]

Dataset: TypeAlias = dict[str, str | list | dict[str, str]]
Transform: TypeAlias = Callable[[DataFrame], DataFrame]


def read_all_datasets(
    datasets: dict[Dataset],
    raw: bool = True,  # True if RAW_DATA, otherwise INTERIM_DATA
) -> tuple[pl.DataFrame, pl.DataFrame]:
    "Read and merge all datasets."
    lfs, metas = [], []
    for dset in datasets.values():
        variables = dset["variables"]
        rename = dset["rename"]

        if raw:
            cols = variables + list(rename.keys())
            df, meta = bk.read_sav(RAW_DATA / dset["file"], usecols=cols)
        else:
            cols = variables + list(rename.values())
            df, meta = bk.read_sav(INTERIM_DATA / dset["file"], usecols=cols)
        lfs.append(df)
        metas.append(meta)

    combined_lf = _concat_lazy_frames(lfs)
    combined_meta = (
        pl.concat(metas, how="vertical")
        .filter(pl.col("Variable").ne("ID"))
        .with_columns(basename=pl.col("Variable").str.slice(5))
    )

    return combined_lf, combined_meta


def _concat_lazy_frames(lfs: list[pl.LazyFrame]) -> pl.LazyFrame:
    return pl.concat(lfs, how="align")


def apply_pipeline(df: DataFrame, transforms: list[Transform]) -> DataFrame:
    "Selectively apply functions in a composable pipeline"
    return reduce(lambda result, fn: fn(result), transforms, df)


def transform_datasets(
    datasets: dict[str, DataFrame], pipelines: dict[str, Transform]
) -> dict[str, DataFrame]:
    "Apply defined transformations to the datasets"
    return {
        dset: apply_pipeline(df, pipelines[dset])
        for dset, df in datasets.items()
        if dset in pipelines
    }


def make_interim(file: Dataset, raw: Path = RAW_DATA) -> tuple[pl.DataFrame, pl.DataFrame]:
    """
    Make the initial transformations from RAW to INTERIM data.
    """
    file_name = file["file"]
    rename = file["rename"]
    delete = file["delete"]

    df, meta = bk.read_sav(raw / file_name)

    df = df.rename(rename).drop(delete)
    meta = meta.with_columns(pl.col("Variable").replace(rename))

    return df, meta


def make_interim_datasets(
    datasets: dict[str, Dataset],
):
    for name, dset in datasets.items():
        df, meta = make_interim(dset, RAW_DATA)
        bk.write_sav(INTERIM_DATA / dset["file"], df, meta)
