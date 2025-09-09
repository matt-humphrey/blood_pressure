import marimo

__generated_with = "0.15.2"
app = marimo.App(width="medium")


@app.cell
def _():
    import re
    from typing import Any

    import banksia as bk
    import marimo as mo
    import pointblank as pb
    import polars as pl
    return mo, pb, pl


@app.cell
def _():
    from blood_pressure import read_all_datasets
    from blood_pressure.config import DATASETS, RAW_DATA
    return DATASETS, read_all_datasets


@app.cell
def _(DATASETS, read_all_datasets):
    df, meta = read_all_datasets(DATASETS)
    return df, meta


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""# Explore by dataset""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## G126""")
    return


@app.cell
def _(df, pl):
    df.select("ID", pl.col("^G126_.*$")).filter(~pl.all_horizontal(pl.exclude("ID").is_null()))
    return


@app.cell
def _(meta, pl):
    meta.filter(pl.col("Variable").str.starts_with("G126"))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## G208""")
    return


@app.cell
def _(df, pl):
    df.select("ID", pl.col("^G208_.*$")).filter(~pl.all_horizontal(pl.exclude("ID").is_null()))
    return


@app.cell
def _(meta, pl):
    meta.filter(pl.col("Variable").str.starts_with("G208"))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## G214""")
    return


@app.cell
def _(df, pl):
    df.select("ID", pl.col("^G214_.*$")).filter(~pl.all_horizontal(pl.exclude("ID").is_null()))
    return


@app.cell
def _(meta, pl):
    meta.filter(pl.col("Variable").str.starts_with("G214"))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## G217""")
    return


@app.cell
def _(df, pl):
    df.select("ID", pl.col("^G217_.*$")).filter(~pl.all_horizontal(pl.exclude("ID").is_null()))
    return


@app.cell
def _(meta, pl):
    meta.filter(pl.col("Variable").str.starts_with("G217"))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## G222""")
    return


@app.cell
def _(df, pl):
    df.select("ID", pl.col("^G222_.*$")).filter(~pl.all_horizontal(pl.exclude("ID").is_null()))
    return


@app.cell
def _(meta, pl):
    meta.filter(pl.col("Variable").str.starts_with("G222"))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    # Explore by variable

    - Confirm type/schema is the same
    - Confirm values are within expected set/range
    - Define metadata
    - Create validation
    - Test validation
    """
    )
    return


@app.cell
def _(meta):
    meta["basename"].unique().sort()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## BP10""")
    return


@app.cell
def _(meta, pl):
    meta.filter(pl.col("basename").eq("BP10"))
    return


@app.cell
def _(df, pl):
    bp10 = df.select(pl.col(r"^G\w{3}_BP10$")).filter(~pl.any_horizontal(pl.all().is_null()))
    bp10
    return (bp10,)


@app.cell
def _(bp10):
    bp10.describe()
    return


@app.cell
def _(bp10, pl):
    bp10.with_columns(pl.col(r"^G\w{3}_BP10$").replace({-99: None, -88: None})).describe()
    return


@app.cell
def _(bp10, pb, pl):
    validation_bp10 = (
        pb.Validate(data=bp10)
        .col_vals_between(
            columns=pb.matches(r"^G\w{3}_BP10$"), 
            left=30, 
            right=108, 
            na_pass=True, 
            pre=lambda df: df.with_columns(pl.col(r"^G\w{3}_BP10$").replace({-99: None, -88: None})),
        )
    ).interrogate()

    validation_bp10
    return


if __name__ == "__main__":
    app.run()
