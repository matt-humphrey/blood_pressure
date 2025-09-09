import marimo

__generated_with = "0.15.2"
app = marimo.App(width="medium")


@app.cell
def _():
    from functools import partial
    from pathlib import Path
    from typing import TypeAlias

    import banksia as bk
    import marimo as mo
    import pointblank as pb
    import polars as pl
    from banksia import Metadata

    return Metadata, pb, pl


@app.cell
def _():
    from blood_pressure import read_all_datasets
    from blood_pressure.config import DATASETS, INTERIM_DATA, METADATA, RAW_DATA

    return DATASETS, METADATA, read_all_datasets


@app.cell
def _(DATASETS, read_all_datasets):
    df, meta = read_all_datasets(DATASETS, raw=False)
    return (df,)


@app.cell
def _():
    variable = r"DM13[A-E]"
    return (variable,)


@app.cell
def _(df, pl, variable):
    dfx = df.select("ID", pl.col(f"^.*{variable}$")).filter(
        ~pl.all_horizontal(pl.exclude("ID").is_null())
    )
    return (dfx,)


@app.cell
def _(dfx, pl):
    dfx_new = dfx.with_columns(pl.all().replace({-99: None, -88: None, 0: None}))
    dfx_new.filter(~pl.all_horizontal(pl.exclude("ID").is_null()))
    return (dfx_new,)


@app.cell
def _(dfx_new, pl):
    dfx_new.unique(subset=pl.exclude("ID"))
    return


@app.cell
def _(dfx_new, pb, variable):
    validate = (
        pb.Validate(data=dfx_new)
        .col_vals_between(columns=pb.matches(variable), left=1, right=26, na_pass=True)
        .interrogate()
    )

    validate
    return


@app.cell
def _(df, pl):
    df_cleaned = (
        df.select("ID", pl.col(r"^G\w{3}_DM\w+$"))
        .filter(~pl.all_horizontal(pl.exclude("ID").is_null()))
        .with_columns(pl.exclude("ID").replace({-88: None, -99: None, 0: None}))
    )
    return (df_cleaned,)


@app.cell
def _(Metadata, pb):
    def create_validation_col_vals_in_set(
        v: pb.Validate, m: Metadata, na_pass: bool = True
    ) -> pb.Validate:
        values = list(m.field_values.keys())
        if na_pass:
            values += [None]
        return v.col_vals_in_set(columns=pb.matches(m.basename), set=values)

    return (create_validation_col_vals_in_set,)


@app.cell
def _(METADATA, create_validation_col_vals_in_set, df_cleaned, pb):
    validation = pb.Validate(df_cleaned)
    for m in METADATA[:10]:
        validation = create_validation_col_vals_in_set(validation, m)

    validation.interrogate()
    return (validation,)


@app.cell
def _(pb, validation):
    validation.get_step_report(i=44, columns_subset=pb.matches("DM4"))
    return


@app.cell
def _(pb, validation):
    validation.get_step_report(i=65, columns_subset=pb.matches("DM17"))
    return


@app.cell
def _(validation):
    validation.get_sundered_data(type="fail")
    return


if __name__ == "__main__":
    app.run()
