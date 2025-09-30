from datetime import time
from typing import Callable

import polars as pl
from polars import DataFrame

__all__ = ["DATA_TRANSFORMS"]


def sort_by_id(df: DataFrame) -> DataFrame:
    return df.sort(by="ID")


def replace_missing_values(df: DataFrame) -> DataFrame:
    """Replace values for specified columns"""
    return df.with_columns(
        pl.col(r"^G\w{3}_BP\d+$").replace({-99: None, -88: None, 999: None}),
        pl.col(r"^G\w{3}_BP[DS][1-6]$").replace({-99: None, -88: None}),
        pl.col(r"^G\w{3}_SHR[1-6]$").replace({-99: None, -88: None}),
        pl.col(r"^G\w{3}_TECH$").replace({-99: None, -88: None}),
    )


def recast_types(df: DataFrame) -> DataFrame:
    """Recast columns with new dtypes"""
    return df.with_columns(
        pl.col(r"^G\w{3}_BP\d+$").cast(pl.Int64),
        pl.col(r"^G\w{3}_BP[DS][1-6]$").cast(pl.Int64),
        pl.col(r"^G\w{3}_SHR[1-6]$").cast(pl.Int64),
        pl.col(r"^G\w{3}_CYC[1-3]$").cast(pl.Int64),
        pl.col(r"^G\w{3}_TECH$").cast(pl.Int64),
        pl.col(r"^G\w{3}_XCAR$").cast(pl.Int64),
    )


def apply_rounding(df: DataFrame) -> DataFrame:
    """Apply rounding to specified float columns"""
    return df.with_columns(
        pl.col(r"^G\w{3}_PWC170$").cast(pl.Float64).round(2),
    )


def recode_bp41(df: DataFrame) -> DataFrame:
    """Replace errant value of 1110 with None."""
    return df.with_columns(pl.col("G214_BP41").replace({1110: None}))


def recode_xcar_g214(df: DataFrame) -> DataFrame:
    """
    Clean XCAR variable for G214.

    Values of 0 were used in two cases where the participant started, but did not finish.
    Values of 9 were used to represent "Missing", which is superfluous, and hence is removed.
    """
    return df.with_columns(pl.col("G214_XCAR").replace({9: None}))


def recode_xcar_g217(df: DataFrame) -> DataFrame:
    """
    Clean XCAR variable for G217.

    To harmonise with G214, values of 0 are removed (because in this case, they were only used when
    the participant did not do the test at all).
    """
    return df.with_columns(pl.col("G217_XCAR").replace({0: None}))


def offset_time(col: str, offset: str = "12h") -> pl.Expr:
    """
    Create a Polars Expression to offset a column with dtype Time by a given amount
    """
    return (
        pl.datetime(2000, 1, 1)  # add arbitary date to enable arithmetic on datetime object
        .dt.combine(pl.col(col))
        .dt.offset_by(offset)
        .dt.time()
        .alias(col)
    )


def update_time_for_g126_slpt(df: DataFrame) -> DataFrame:
    """
    Convert times from AM to PM for `G126_SLPT`.

    This function converts the time column to a datetime object, because Polars can't perform
    arithmetic on time objects, and adds 12 hours, before converting back to a time object.
    """
    return df.with_columns(offset_time("G126_SLPT", "12h"))


def update_time_for_g126_bpsl(df: DataFrame) -> DataFrame:
    """
    Convert mislabelled times from AM to PM

    Only one notable instance for ID 4801 (10:16 -> 22:16)
    """
    return df.with_columns(
        pl.when(pl.col("G126_BPSL").is_between(time(1), time(12)))
        .then(offset_time("G126_BPSL", "12h"))
        .otherwise(pl.col("G126_BPSL"))
        .alias("G126_BPSL")
    )


def update_time_for_g222_slpt(df: DataFrame) -> DataFrame:
    """
    Convert mislabelled times from AM to PM
    """
    return df.with_columns(
        pl.when(pl.col("G222_SLPT").is_between(time(10), time(12)))
        .then(offset_time("G222_SLPT", "12h"))
        .otherwise(pl.col("G222_SLPT"))
        .alias("G222_SLPT")
    )


def clean_string_column(col: str) -> Callable:
    """Clean string column by removing escape sequences."""

    def preprocessor(df: DataFrame) -> DataFrame:
        return df.with_columns(
            pl.col(col)
            .str.replace_all(r"^[\n\r]+", "", literal=False)  # Remove escape chars at start
            .str.replace_all(r"[\n\r]+", "; ", literal=False)  # Replace escape chars with semicolon
            .str.replace_all(r"\s+", " ", literal=False)  # Collapse multiple spaces
            .str.strip_chars()  # Remove leading/trailing whitespace
            .alias(col)
        )

    return preprocessor


initial_transforms = [replace_missing_values]
final_transforms = [recast_types, sort_by_id]

dataset_transforms = {
    "G126": [update_time_for_g126_slpt, clean_string_column("G126_SL_COM")],
    "G208": [],
    "G214": [apply_rounding, recode_bp41, recode_xcar_g214],
    "G217": [apply_rounding, recode_xcar_g217],
    "G222": [update_time_for_g222_slpt, clean_string_column("G222_SL_COM")],
}

DATA_TRANSFORMS = {
    dset: initial_transforms + transforms + final_transforms
    for dset, transforms in dataset_transforms.items()
}
