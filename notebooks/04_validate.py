import marimo

__generated_with = "0.15.2"
app = marimo.App(width="medium")


@app.cell
def _():
    import banksia as bk
    import marimo as mo
    import pointblank as pb
    import polars as pl
    import pyreadstat
    from pointblank import Validate

    return Validate, bk, pb, pl


@app.cell
def _():
    from blood_pressure import (  # create_validation_col_vals_in_set
        DATA_TRANSFORMS,
        VALIDATIONS,
        apply_pipeline,
        make_interim_datasets,
        transform_datasets,
    )
    from blood_pressure.config import DATASETS, INTERIM_DATA, METADATA, PROCESSED_DATA, RAW_DATA

    return DATASETS, METADATA, PROCESSED_DATA


@app.cell
def _(DATASETS, PROCESSED_DATA, bk):
    dfs, metas = {}, {}

    for name, dset in DATASETS.items():
        file = dset["file"]
        df, meta = bk.read_sav(PROCESSED_DATA / file)
        dfs[name] = df
        metas[name] = meta
    return dfs, metas


@app.cell
def _(Validate, bk, pb):
    def create_validation_col_vals_in_set(
        v: Validate, m: bk.Metadata, na_pass: bool = True
    ) -> Validate:
        values = list(m.field_values.keys())
        if na_pass:
            values += [None]
        return v.col_vals_in_set(columns=pb.matches(m.basename), set=values)

    return (create_validation_col_vals_in_set,)


@app.cell
def _(metas, pl):
    metas["G201"].filter(pl.col("Variable").str.contains("DM"))
    return


@app.cell
def _(METADATA):
    METADATA
    return


@app.cell
def _(Validate, create_validation_col_vals_in_set, dfs, metas):
    dx = "G201"
    v = Validate(data=dfs[dx])
    create_validation_col_vals_in_set(v, metas[dx])
    # apply_pipeline(v, FINAL_VALIDATIONS[dx]).interrogate()
    return


@app.cell
def _():
    # dfs["G214"].filter(pl.col("G214_BP47").lt(30)).select("ID", "G214_BP47")
    return


if __name__ == "__main__":
    app.run()
