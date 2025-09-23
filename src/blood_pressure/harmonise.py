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


def update_time_for_g126_slpt(df: DataFrame) -> DataFrame:
    """
    Convert times from AM to PM for `G126_SLPT`.

    This function converts the time column to a datetime object, because Polars can't perform
    arithmetic on time objects, and adds 12 hours, before converting back to a time object.
    """
    return df.with_columns(
        pl.datetime(2000, 1, 1)  # add arbitary date to enable arithmetic on datetime object
        .dt.combine(pl.col("G126_SLPT"))
        .dt.offset_by("12h")
        .dt.time()
        .alias("G126_SLPT")
    )


initial_transforms = [replace_missing_values]
final_transforms = [recast_types, sort_by_id]

dataset_transforms = {
    "G126": [update_time_for_g126_slpt],
    "G208": [],
    "G214": [apply_rounding, recode_bp41, recode_xcar_g214],
    "G217": [apply_rounding, recode_xcar_g217],
    "G222": [],
}

DATA_TRANSFORMS = {
    dset: initial_transforms + transforms + final_transforms
    for dset, transforms in dataset_transforms.items()
}
