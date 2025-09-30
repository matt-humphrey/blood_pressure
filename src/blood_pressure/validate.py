from datetime import time

import pointblank as pb
import polars as pl
from banksia import Metadata
from pointblank import Validate

__all__ = ["VALIDATIONS"]

# TODO: create generic validation function which tests values in set for metadata with field values


def create_validation_col_vals_in_set(v: Validate, m: Metadata, na_pass: bool = True) -> Validate:
    values = list(m.field_values.keys())
    if na_pass:
        values += [None]
    return v.col_vals_in_set(columns=pb.matches(m.basename), set=values)


def validate_cycling_baseline(validation: Validate) -> Validate:
    return (
        validation.col_vals_between(
            columns=pb.matches(r"^G\w{3}_BP9$"), left=65, right=169, na_pass=True
        )
        .col_vals_between(columns=pb.matches(r"^G\w{3}_BP10$"), left=30, right=114, na_pass=True)
        .col_vals_between(columns=pb.matches(r"^G\w{3}_BP11$"), left=45, right=137, na_pass=True)
        .col_vals_in_set(columns=pb.matches(r"^G\w{3}_TECH$"), set=[1, 2, 3, None])
    )


def validate_cycling(validation: Validate) -> Validate:
    return (
        validation.col_vals_in_set(columns=pb.matches(r"^G\w{3}_BP12"), set=[1, 2, None])
        .col_vals_between(columns=pb.matches(r"^G\w{3}_BP13$"), left=56, right=152, na_pass=True)
        .col_vals_between(columns=pb.matches(r"^G\w{3}_BP14$"), left=46, right=173, na_pass=True)
        .col_vals_between(columns=pb.matches(r"^G\w{3}_BP15$"), left=45, right=188, na_pass=True)
        .col_vals_between(columns=pb.matches(r"^G\w{3}_BP16$"), left=58, right=199, na_pass=True)
        .col_vals_between(columns=pb.matches(r"^G\w{3}_BP17$"), left=58, right=181, na_pass=True)
        .col_vals_between(columns=pb.matches(r"^G\w{3}_BP18$"), left=52, right=189, na_pass=True)
        .col_vals_between(columns=pb.matches(r"^G\w{3}_PWC170$"), left=25, right=344, na_pass=True)
        .col_vals_in_set(columns=pb.matches(r"^G\w{3}_XCAR$"), set=[0, 1, None])
    )


def validate_cycling_g208(validation: Validate) -> Validate:
    return (
        validation.col_vals_between(
            columns=pb.matches(r"^G\w{3}_BP82$"), left=48, right=195, na_pass=True
        )
        .col_vals_between(columns=pb.matches(r"^G\w{3}_BP83$"), left=20, right=144, na_pass=True)
        .col_vals_between(columns=pb.matches(r"^G\w{3}_BP84$"), left=29, right=166, na_pass=True)
        .col_vals_between(columns=pb.matches(r"^G\w{3}_BP85$"), left=45, right=197, na_pass=True)
        .col_vals_between(columns=pb.matches(r"^G\w{3}_BP86$"), left=19, right=158, na_pass=True)
        .col_vals_between(columns=pb.matches(r"^G\w{3}_BP87$"), left=37, right=173, na_pass=True)
        .col_vals_between(columns=pb.matches(r"^G\w{3}_BP88$"), left=33, right=229, na_pass=True)
        .col_vals_between(columns=pb.matches(r"^G\w{3}_BP89$"), left=27, right=192, na_pass=True)
        .col_vals_between(columns=pb.matches(r"^G\w{3}_BP90$"), left=45, right=186, na_pass=True)
    )


def validate_post_cycling_blood_pressure(validation: Validate) -> Validate:
    return (
        validation.col_vals_in_set(
            columns=pb.matches(r"^G\w{3}_BP(24|28|32|36|40|44)$"), set=[1, 2, None]
        )
        .col_vals_between(columns=pb.matches(r"^G\w{3}_BP21$"), left=68, right=217, na_pass=True)
        .col_vals_between(columns=pb.matches(r"^G\w{3}_BP22$"), left=31, right=128, na_pass=True)
        .col_vals_between(columns=pb.matches(r"^G\w{3}_BP23$"), left=51, right=173, na_pass=True)
        .col_vals_between(columns=pb.matches(r"^G\w{3}_BP25$"), left=68, right=213, na_pass=True)
        .col_vals_between(columns=pb.matches(r"^G\w{3}_BP26$"), left=33, right=119, na_pass=True)
        .col_vals_between(columns=pb.matches(r"^G\w{3}_BP27$"), left=49, right=153, na_pass=True)
        .col_vals_between(columns=pb.matches(r"^G\w{3}_BP29$"), left=61, right=186, na_pass=True)
        .col_vals_between(columns=pb.matches(r"^G\w{3}_BP30$"), left=32, right=108, na_pass=True)
        .col_vals_between(columns=pb.matches(r"^G\w{3}_BP31$"), left=47, right=148, na_pass=True)
        .col_vals_between(columns=pb.matches(r"^G\w{3}_BP33$"), left=79, right=183, na_pass=True)
        .col_vals_between(columns=pb.matches(r"^G\w{3}_BP34$"), left=31, right=102, na_pass=True)
        .col_vals_between(columns=pb.matches(r"^G\w{3}_BP35$"), left=46, right=137, na_pass=True)
        .col_vals_between(columns=pb.matches(r"^G\w{3}_BP37$"), left=53, right=177, na_pass=True)
        .col_vals_between(columns=pb.matches(r"^G\w{3}_BP38$"), left=27, right=100, na_pass=True)
        .col_vals_between(columns=pb.matches(r"^G\w{3}_BP39$"), left=50, right=142, na_pass=True)
        .col_vals_between(columns=pb.matches(r"^G\w{3}_BP41$"), left=67, right=166, na_pass=True)
        .col_vals_between(columns=pb.matches(r"^G\w{3}_BP42$"), left=34, right=97, na_pass=True)
        .col_vals_between(columns=pb.matches(r"^G\w{3}_BP43$"), left=55, right=140, na_pass=True)
    )


def validate_sleep_blood_pressure(validation: Validate) -> Validate:
    return (
        validation.col_vals_between(
            columns=pb.matches(r"^G\w{3}_BPS[1-6]$"), left=64, right=237, na_pass=True
        )
        .col_vals_between(
            columns=pb.matches(r"^G\w{3}_BPD[1-6]$"), left=27, right=135, na_pass=True
        )
        .col_vals_between(
            columns=pb.matches(r"^G\w{3}_SHR[1-6]$"), left=31, right=130, na_pass=True
        )
    )


def validate_sleep_times(validation: Validate) -> Validate:
    return validation.col_vals_expr(
        expr=pl.col(r"^G\w{3}_BPSL$").is_between(time(19, 30), time(23, 59))
    ).col_vals_expr(
        expr=pl.col(r"^G\w{3}_SLPT$").is_between(time(19, 30), time(23, 59))
        | pl.col(r"^G\w{3}_SLPT$").is_between(time(0), time(1))
    )


VALIDATIONS = {
    "G126": [validate_sleep_blood_pressure, validate_sleep_times],
    "G208": [
        validate_cycling_baseline,
        validate_cycling_g208,
        validate_post_cycling_blood_pressure,
    ],
    "G214": [validate_cycling_baseline, validate_cycling, validate_post_cycling_blood_pressure],
    "G217": [validate_cycling_baseline, validate_cycling, validate_post_cycling_blood_pressure],
    "G222": [validate_sleep_blood_pressure, validate_sleep_times],
}
