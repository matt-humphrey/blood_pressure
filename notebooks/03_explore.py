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
    from datetime import time
    return bk, mo, pb, pl, time


@app.cell
def _():
    from blood_pressure import read_all_datasets
    from blood_pressure.config import DATASETS, RAW_DATA
    return DATASETS, RAW_DATA, read_all_datasets


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


@app.cell(hide_code=True)
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
            left=31,
            right=130,
            na_pass=True,
            pre=lambda df: df.with_columns(pl.col(r"^.*SHR\d$").replace({-99: None, -88: None})),
        )
        .interrogate()
    )

    validation_shr
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## Miscellaneous""")
    return


@app.cell
def _(meta, pl):
    m_misc = meta.filter(
        pl.col("basename").is_in(["SLPT", "WKBP", "WKT", "BPSL", "SPRAT"])
    ).sort(by="basename")
    cols_misc = m_misc.to_series(0).to_list()
    m_misc
    return (cols_misc,)


@app.cell
def _(cols_misc, df, pl):
    df.select(cols_misc).filter(~pl.all_horizontal(pl.exclude("ID").is_null())).describe()
    return


@app.cell
def _(df, pl):
    # Convert G216_SLPT to evening time - add 12 hours
    df.with_columns(
        pl.datetime(2000, 1, 1) # add arbitary date to enable arithmetic on datetime object
        .dt.combine(pl.col("G126_SLPT"))
        .dt.offset_by("12h")
        .dt.time()
        .alias("G126_SLPT")
    )
    return


@app.cell
def _(pl):
    def update_time_for_g126_slpt(df: pl.DataFrame) -> pl.DataFrame:
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
    return (update_time_for_g126_slpt,)


@app.cell
def _(df, pb, update_time_for_g126_slpt):
    # Create validations to check that sleeping time (SLPT) was after blood pressure before sleep (BPSL)
    # And likewise that waking time (WKT) was before blood pressure after waking (WKBP)

    validate_slp = (
        pb.Validate(data=df)
        .col_vals_ge(
            columns="G126_SLPT",
            value=pb.col("G126_BPSL"),
            na_pass=True,
            pre=update_time_for_g126_slpt,
        )
        .col_vals_ge(
            columns="G126_WKBP",
            value=pb.col("G126_WKT"),
            na_pass=True,
        )
        .col_vals_ge(
            columns="G222_SLPT",
            value=pb.col("G222_BPSL"),
            na_pass=True,
        )
        .col_vals_ge(
            columns="G222_WKBP",
            value=pb.col("G222_WKT"),
            na_pass=True,
        )
        .interrogate()
    )

    validate_slp
    return (validate_slp,)


@app.cell
def _(pb, validate_slp):
    validate_slp.get_step_report(1, columns_subset=pb.matches("ID|G126_(SLPT|BPSL)"))
    return


@app.cell
def _(pb, validate_slp):
    validate_slp.get_step_report(2, columns_subset=pb.matches("ID|G126_(WKBP|WKT)"))
    return


@app.cell
def _(pb, validate_slp):
    validate_slp.get_step_report(3, columns_subset=pb.matches("ID|G222_(SLPT|BPSL)"))
    return


@app.cell
def _(pb, validate_slp):
    validate_slp.get_step_report(4, columns_subset=pb.matches("ID|G222_(WKBP|WKT)"))
    return


@app.cell
def _(df, pl):
    # Investigate cases for G222_WKT that were in the afternoon/evening
    df.select("ID", "G222_SLPT", "G222_WKT").filter(pl.col("G222_WKT").is_not_null()).sort(by="G222_WKT", descending=True).head()
    return


@app.cell
def _(df, pl):
    # Investigate cases for G222_SPRAT where the set up time was in the morning (in one case at 2am?)
    df.select("ID", "G222_SPRAT").filter(pl.col("G222_SPRAT").is_not_null()).sort(by="G222_SPRAT", descending=False).head()
    return


@app.cell
def _():
    # validation_misc = (
    #     pb.Validate(data=df)
    #     .col_vals_between(
    #         columns=pb.matches(r"SHR\d"),
    #         left=27,
    #         right=135,
    #         na_pass=True,
    #         pre=lambda df: df.with_columns(pl.col(r"^.*SHR\d$").replace({-99: None, -88: None})),
    #     )
    #     .interrogate()
    # )

    # validation_misc
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## Check `G222_BP_TIME`""")
    return


@app.cell
def _(RAW_DATA, pl):
    bp_time = pl.read_csv(RAW_DATA/"BPTIME.csv", has_header=False, new_columns=["ID", "G222_BP_TIME"], schema={"ID": pl.Utf8, "G222_BP_TIME": pl.Time})
    bp_time = bp_time.with_columns(pl.col("ID").str.strip_chars().cast(pl.Float64)).sort(by="ID")
    bp_time
    return (bp_time,)


@app.cell
def _(RAW_DATA, bk):
    g222, _ = bk.read_sav(RAW_DATA/"G222_PA.sav")
    g222 = g222.select("ID", "G222_BP_TIME")
    g222
    return (g222,)


@app.cell
def _(bp_time, g222):
    df_bp = g222.join(bp_time, on="ID", how="full").drop("ID_right")
    df_bp
    return (df_bp,)


@app.cell
def _(pl):
    def update_time_for_g222_bp_time(df: pl.DataFrame) -> pl.DataFrame:
        return df.with_columns(
            pl.datetime(2000, 1, 1)  # add arbitary date to enable arithmetic on datetime object
            .dt.combine(pl.col("G222_BP_TIME"))
            .dt.offset_by("12h")
            .dt.time()
            .alias("G222_BP_TIME")
        )
    return


@app.cell
def _(df_bp, pl):
    df_bp.filter(pl.col("G222_BP_TIME").ne(pl.col("G222_BP_TIME_right")))
    return


@app.cell
def _(df_bp, pl, time):
    df_bp.filter(pl.col("G222_BP_TIME_right").is_between(time(5), time(12)))
    return


@app.cell
def _(df_bp, pl, time):
    # A handful of cases with difficult times to determine
    df_bp.filter(pl.col("G222_BP_TIME_right").is_between(time(12), time(17)))
    return


@app.cell
def _(df_bp, pl, time):
    df_bp.filter(pl.col("G222_BP_TIME_right").is_between(time(17), time(23, 59)))
    return


@app.cell
def _(df_bp, pb, pl, time):
    validate_bp = pb.Validate(data=df_bp).col_vals_expr(expr=pl.col("G222_BP_TIME_right").is_between(time(5), time(12))).interrogate()

    validate_bp
    return


if __name__ == "__main__":
    app.run()
