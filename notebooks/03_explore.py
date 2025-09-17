import marimo

__generated_with = "0.15.5"
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
    from blood_pressure.config import DATASETS

    return DATASETS, read_all_datasets


@app.cell
def _(DATASETS, read_all_datasets):
    df, meta = read_all_datasets(DATASETS)
    return df, meta


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
    mo.md(r"""## `BPS1` to `BPS8`""")
    return


@app.cell
def _(meta, pl):
    m_bps = meta.filter(pl.col("basename").str.contains(r"BPS\d$")).sort(by="basename")
    cols_bps = m_bps.to_series(0).to_list()
    m_bps
    return (cols_bps,)


@app.cell
def _(cols_bps, df, pl):
    df.select(cols_bps).filter(~pl.all_horizontal(pl.exclude("ID").is_null())).with_columns(
        pl.all().replace({-99: None, -88: None})
    ).describe()
    return


@app.cell
def _(df, pb, pl):
    test = df.with_columns(
        G126_BPS_avg1=pl.mean_horizontal(pl.col("^G126_BPS[1-3]$")).round(1),
        G126_BPS_avg2=pl.mean_horizontal(pl.col("^G126_BPS[4-6]$")).round(1),
        G222_BPS_avg1=pl.mean_horizontal(pl.col("^G222_BPS[1-3]$")).round(1),
        G222_BPS_avg2=pl.mean_horizontal(pl.col("^G222_BPS[4-6]$")).round(1),
    )

    validate_test = (
        pb.Validate(data=test)
        .col_vals_eq("G126_BPS7", value=pb.col("G126_BPS_avg1"), na_pass=True)
        .col_vals_eq("G126_BPS8", value=pb.col("G126_BPS_avg2"), na_pass=True)
        .col_vals_eq("G222_BPS7", value=pb.col("G222_BPS_avg1"), na_pass=True)
        .col_vals_eq("G222_BPS8", value=pb.col("G222_BPS_avg2"), na_pass=True)
    )

    validate_test.interrogate()
    return test, validate_test


@app.cell
def _(pb, validate_test):
    validate_test.get_step_report(2, columns_subset=pb.matches("G126_BPS"))
    return


@app.cell
def _(pl, test):
    test.select("ID", pl.col("^G126_BPS[4-6]$", "G126_BPS8", "G126_BPS_avg2"))
    return


@app.cell
def _(df, pl):
    df.with_columns(pl.col("G126_BPS8") == pl.mean_horizontal(pl.col("^G126_BPS[4-6]$")))
    return


@app.cell
def _(df, pb, pl):
    validation_bps = (
        pb.Validate(data=df)
        .col_vals_between(
            columns=pb.matches(r"BPS\d"),
            left=64,
            right=237,
            na_pass=True,
            pre=lambda df: df.with_columns(pl.col(r"^.*BPS\d$").replace({-99: None, -88: None})),
        )
        .interrogate()
    )

    validation_bps
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## `BPD1` to `BPD8`""")
    return


@app.cell
def _(meta, pl):
    m_bpd = meta.filter(pl.col("basename").str.contains(r"BPD\d$")).sort(by="basename")
    cols_bpd = m_bpd.to_series(0).to_list()
    m_bpd
    return (cols_bpd,)


@app.cell
def _(cols_bpd, df, pl):
    df.select(cols_bpd).filter(~pl.all_horizontal(pl.exclude("ID").is_null())).with_columns(
        pl.all().replace({-99: None, -88: None})
    ).describe()
    return


@app.cell
def _(df, pb, pl):
    test_bpd = df.with_columns(
        G126_BPD_avg1=pl.mean_horizontal(pl.col("^G126_BPD[1-3]$")).round(1),
        G126_BPD_avg2=pl.mean_horizontal(pl.col("^G126_BPD[4-6]$")).round(1),
        G222_BPD_avg1=pl.mean_horizontal(pl.col("^G222_BPD[1-3]$")).round(1),
        G222_BPD_avg2=pl.mean_horizontal(pl.col("^G222_BPD[4-6]$")).round(1),
    )

    validate_test_bpd = (
        pb.Validate(data=test_bpd)
        .col_vals_eq("G126_BPD7", value=pb.col("G126_BPD_avg1"), na_pass=True)
        .col_vals_eq("G126_BPD8", value=pb.col("G126_BPD_avg2"), na_pass=True)
        .col_vals_eq("G222_BPD7", value=pb.col("G222_BPD_avg1"), na_pass=True)
        .col_vals_eq("G222_BPD8", value=pb.col("G222_BPD_avg2"), na_pass=True)
    )

    validate_test_bpd.interrogate()
    return


@app.cell
def _(df, pb, pl):
    validation_bpd = (
        pb.Validate(data=df)
        .col_vals_between(
            columns=pb.matches(r"BPD\d"),
            left=27,
            right=135,
            na_pass=True,
            pre=lambda df: df.with_columns(pl.col(r"^.*BPD\d$").replace({-99: None, -88: None})),
        )
        .interrogate()
    )

    validation_bpd
    return


@app.cell
def _(mo):
    mo.md(r"""## `SHR1` to `SHR8`""")
    return


@app.cell
def _(meta, pl):
    m_shr = meta.filter(pl.col("basename").str.contains(r"SHR\d$")).sort(by="basename")
    cols_shr = m_shr.to_series(0).to_list()
    m_shr
    return (cols_shr,)


@app.cell
def _(cols_shr, df, pl):
    df.select(cols_shr).filter(~pl.all_horizontal(pl.exclude("ID").is_null())).with_columns(
        pl.all().replace({-99: None, -88: None})
    ).describe()
    return


@app.cell
def _(df, pb, pl):
    test_shr = df.with_columns(
        G126_shr_avg1=pl.mean_horizontal(pl.col("^G126_SHR[1-3]$")).round(1),
        G126_shr_avg2=pl.mean_horizontal(pl.col("^G126_SHR[4-6]$")).round(1),
        G222_shr_avg1=pl.mean_horizontal(pl.col("^G222_SHR[1-3]$")).round(1),
        G222_shr_avg2=pl.mean_horizontal(pl.col("^G222_SHR[4-6]$")).round(1),
    )

    validate_test_shr = (
        pb.Validate(data=test_shr)
        .col_vals_eq("G126_SHR7", value=pb.col("G126_shr_avg1"), na_pass=True)
        .col_vals_eq("G126_SHR8", value=pb.col("G126_shr_avg2"), na_pass=True)
        .col_vals_eq("G222_SHR7", value=pb.col("G222_shr_avg1"), na_pass=True)
        .col_vals_eq("G222_SHR8", value=pb.col("G222_shr_avg2"), na_pass=True)
    )

    validate_test_shr.interrogate()
    return


@app.cell
def _(df, pb, pl):
    validation_shr = (
        pb.Validate(data=df)
        .col_vals_between(
            columns=pb.matches(r"SHR\d"),
            left=27,
            right=135,
            na_pass=True,
            pre=lambda df: df.with_columns(pl.col(r"^.*SHR\d$").replace({-99: None, -88: None})),
        )
        .interrogate()
    )

    validation_shr
    return


if __name__ == "__main__":
    app.run()
