import pytest

import banksia as bk
import pointblank as pb
import polars as pl
import polars.selectors as cs

from pathlib import Path
from polars.testing import assert_frame_equal
from typing import Any

from blood_pressure import VALIDATIONS, apply_pipeline
from blood_pressure.config import DATASETS, INTERIM_DATA, METADATA, PROCESSED_DATA, RAW_DATA


def assert_validations_pass(dset: str):
    """Reusable function to assert all validations for a given dataset are passing"""
    df, _meta = bk.read_sav(PROCESSED_DATA / DATASETS[dset]["file"])
    validation = pb.Validate(df)
    validation = apply_pipeline(validation, VALIDATIONS[dset]).interrogate()
    validation.assert_passing()


def validate_raw_to_interim(dset: str):
    """
    Reusable function to validate changes between raw and interim datasets.

    Update the raw data and metadata with variable renaming and dropping variables to be deleted and
    assert both dataframes otherwise remain identical.
    """
    ds = DATASETS[dset]

    df_int, meta_int = bk.read_sav(INTERIM_DATA / ds["file"])
    df_raw, meta_raw = bk.read_sav(RAW_DATA / ds["file"])

    # Cast Null columns as String to match interim data
    null = df_raw.select(cs.by_dtype(pl.Null))
    df_raw_updated = (
        df_raw.rename(ds["rename"])
        .drop(ds["delete"])
        .with_columns(pl.col(null.columns).cast(pl.Utf8).replace({None: ""}))
    )
    meta_raw_updated = meta_raw.with_columns(pl.col("Variable").replace(ds["rename"])).filter(
        ~pl.col("Variable").is_in(ds["delete"])
    )

    assert_frame_equal(df_raw_updated, df_int)
    assert_frame_equal(meta_raw_updated, meta_int)


@pytest.mark.parametrize("dset", ["G126", "G208", "G214", "G217", "G222"])
def test_validate_dataset(dset):
    validate_raw_to_interim(dset)
    assert_validations_pass(dset)
