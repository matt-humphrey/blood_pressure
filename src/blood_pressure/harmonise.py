import polars as pl
from polars import DataFrame

__all__ = ["DATA_TRANSFORMS"]


def sort_by_id(df: DataFrame) -> DataFrame:
    return df.sort(by="ID")


def replace_missing_values(df: DataFrame) -> DataFrame:
    """Replace values for each given column that..."""
    return df.with_columns(
        # pl.col(r"^G\w{3}_DM\d{1,2}[A-Z]$").replace({-99: None, -88: None}),
    )


def recast_types(df: DataFrame) -> DataFrame:
    """Recast column types as new type"""
    return df.with_columns(
        # pl.col(r"^G\w{3}_DM\d{1,2}[A-E]$").cast(pl.Int64),
    )


initial_transforms = [replace_missing_values]
final_transforms = [recast_types, sort_by_id]

dataset_transforms = {
    "G126": [],
    "G208": [],
    "G214": [],
    "G217": [],
    "G222": [],
}

DATA_TRANSFORMS = {
    dset: initial_transforms + transforms + final_transforms
    for dset, transforms in dataset_transforms.items()
}
