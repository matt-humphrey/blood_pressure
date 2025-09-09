import pointblank as pb
import polars as pl
from banksia import Metadata
from pointblank import Validate

# TODO: create generic validation function which tests values in set for metadata with field values


def create_validation_col_vals_in_set(v: Validate, m: Metadata, na_pass: bool = True) -> Validate:
    values = list(m.field_values.keys())
    if na_pass:
        values += [None]
    return v.col_vals_in_set(columns=pb.matches(m.basename), set=values)


def validate_bp10(validation: Validate) -> Validate:
    return validation.col_vals_between(
        columns=pb.matches(r"^G\w{3}_BP10$"), left=30, right=108, na_pass=True
    )


VALIDATIONS = {
    "BP10": validate_bp10,
}
