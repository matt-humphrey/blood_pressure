from datetime import time
from typing import Callable

import polars as pl
from polars import DataFrame

from blood_pressure.config import RAW_DATA

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


def round_time(col: str, by: str = "1m") -> pl.Expr:
    """
    Create a Polars Expression to offset a column with dtype Time by a given amount.

    This function converts the time column to a datetime object, because Polars can't perform
    arithmetic on time objects, and adds 12 hours, before converting back to a time object.
    """
    return (
        pl.datetime(2000, 1, 1)  # add arbitary date to enable arithmetic on datetime object
        .dt.combine(pl.col(col))
        .dt.round(by)
        .dt.time()
        .alias(col)
    )


def update_g126_slpt(df: DataFrame) -> DataFrame:
    """
    Convert times from AM to PM for `G126_SLPT`.
    """
    return df.with_columns(offset_time("G126_SLPT", "12h"))


def update_g222_bp_time(df: DataFrame) -> DataFrame:
    """
    The raw data for many of the values for G222_BP_TIME ended in 59 seconds (ie. 17:50:59).
    This data must have been changed somehow, because data from FileMaker had no seconds value.
    Furthermore, a number of values from FileMaker didn't match what was in core, primarily cases
    where the value was offset by 12 hours (where it was captured as PM, but should have been AM).

    This function reads the data pulled out of FileMaker, formats it, merges with what's in core,
    and then corrects values from it that are suspect and have been captured as AM but should be PM.
    (Data from FileMaker has correctly converted many values from PM to AM, but also "corrected"
    values which should have remained as PM, and hence are being converted back).

    There are values that range between 9am and 5pm, which are considered unusual, given that this
    was a sleep study, and most blood pressures were captured in the evening, from 6pm onwards.
    For all values for `G222_BP_TIME` before 12pm, if there was data for various sleep variables
    captured, convert to PM, and otherwise keep as is - some assessments were done in the morning
    (or afternoon) if the participant did not partake in the sleep study.
    """
    updated_bp_time = pl.read_csv(
        RAW_DATA / "BPTIME.csv",
        has_header=False,
        new_columns=["ID", "G222_BP_TIME"],
        schema={"ID": pl.Utf8, "G222_BP_TIME": pl.Time},
    )
    cleaned_updated_bp_time = updated_bp_time.with_columns(
        pl.col("ID").str.strip_chars_end().cast(pl.Float64)
    )
    df_updated = df.update(cleaned_updated_bp_time, on="ID")

    return df_updated.with_columns(
        pl.when(
            pl.col("G222_BP_TIME").lt(time(12))
            & ~pl.all_horizontal(pl.col(r"^G222_(BPSL|SLPT|WKT|WKP|DNWN_PSG)$").is_null())
        )
        .then(offset_time("G222_BP_TIME"))
        .otherwise(pl.col("G222_BP_TIME"))
        .alias("G222_BP_TIME")
    )


def update_g222_slpt(df: DataFrame) -> DataFrame:
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


def update_g126_bpsl(df: DataFrame) -> DataFrame:
    """
    Update the values of `G126_BPSL` for instances where the value was incorrectly entered.
    """
    new_g126_bpsl = {
        "ID": [
            802,
            1601,
            3701,
            4801,
            55801,
            64101,
            67201,
            68502,
            87401,
            93301,
            94702,
            95501,
            104502,
            114802,
            157701,
            186101,
            200902,
            207901,
            215701,
            225002,
        ],
        "G126_BPSL": [
            time(21, 45),
            time(22),
            time(21, 35),
            time(22, 16),
            time(22, 5),
            time(22),
            time(22),
            time(22, 35),
            time(21, 1),
            time(21, 30),
            time(21, 23),
            time(20, 45),
            time(21),
            time(21),
            time(22, 19),
            time(22, 19),
            time(21, 35),
            time(22, 6),
            time(21, 58),
            time(23, 15),
        ],
    }

    df_new_g126_bpsl = pl.DataFrame(new_g126_bpsl, schema={"ID": pl.Float64, "G126_BPSL": pl.Time})
    return df.update(df_new_g126_bpsl, on="ID")


def update_g222_wkt(df: DataFrame) -> DataFrame:
    """
    Update the values of `G222_WKT` for instances where the value was incorrectly entered.
    """
    new_g222_wkt = {
        "ID": [15900, 17130, 17830, 41310, 41730, 44100],
        "G222_WKT": [time(5, 45), time(6, 25), time(6, 15), time(6), time(5, 47), time(6, 15)],
    }

    df_new_g222_wkt = pl.DataFrame(new_g222_wkt, schema={"ID": pl.Float64, "G222_WKT": pl.Time})
    return df.update(df_new_g222_wkt, on="ID")


initial_transforms = [replace_missing_values]
final_transforms = [recast_types, sort_by_id]

dataset_transforms = {
    "G126": [
        update_g126_slpt,
        update_g126_bpsl,
        clean_string_column("G126_SL_COM"),
    ],
    "G208": [],
    "G214": [apply_rounding, recode_bp41, recode_xcar_g214],
    "G217": [apply_rounding, recode_xcar_g217],
    "G222": [
        update_g222_slpt,
        update_g222_bp_time,
        update_g222_wkt,
        clean_string_column("G222_SL_COM"),
    ],
}

DATA_TRANSFORMS = {
    dset: initial_transforms + transforms + final_transforms
    for dset, transforms in dataset_transforms.items()
}
