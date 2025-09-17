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


@app.cell
def _(mo):
    mo.md(r"""## `BP9`""")
    return


@app.cell
def _(meta, pl):
    m_bp9 = meta.filter(pl.col("basename").str.contains(r"BP9")).sort(by="basename")
    cols_bp9 = m_bp9.to_series(0).to_list()
    m_bp9
    return (cols_bp9,)


@app.cell
def _(cols_bp9, df, pl):
    df.select(cols_bp9).filter(~pl.all_horizontal(pl.exclude("ID").is_null())).with_columns(
        pl.all().replace({-99: None, -88: None})
    ).describe()
    return


@app.cell
def _(df, pb, pl):
    validation_bp9 = (
        pb.Validate(data=df).col_vals_between(
            columns=pb.matches(r"^G\w{3}_BP9$"),
            left=65,
            right=169,
            na_pass=True,
            pre=lambda df: df.with_columns(pl.col(r"^G\w{3}_BP9$").replace({-99: None, -88: None})),
        )
    ).interrogate()

    validation_bp9
    return


@app.cell
def _(mo):
    mo.md(r"""## `BP45`""")
    return


@app.cell
def _(meta, pl):
    m_bp45 = meta.filter(pl.col("basename").str.contains(r"BP45")).sort(by="basename")
    cols_bp45 = m_bp45.to_series(0).to_list()
    m_bp45
    return (cols_bp45,)


@app.cell
def _(cols_bp45, df, pl):
    df.select(cols_bp45).filter(~pl.all_horizontal(pl.exclude("ID").is_null())).with_columns(
        pl.all().replace({-99: None, -88: None})
    ).describe()
    return


@app.cell
def _(df, pb, pl):
    validation_bp45 = (
        pb.Validate(data=df).col_vals_in_set(
            columns=pb.matches(r"^G\w{3}_BP45$"),
            set=[1, 2, None],
            pre=lambda df: df.with_columns(
                pl.col(r"^G\w{3}_BP45$").replace({-99: None, -88: None})
            ),
        )
    ).interrogate()

    validation_bp45
    return


@app.cell
def _(mo):
    mo.md(r"""## G208 Exercise Variables - `BP12_2` to `BP20_2`""")
    return


@app.cell
def _(meta, pl):
    m_bp12 = meta.filter(pl.col("basename").str.contains(r"BP\d{2}_2")).sort(by="basename")
    cols_bp12 = m_bp12.to_series(0).to_list()
    m_bp12
    return (cols_bp12,)


@app.cell
def _(cols_bp12, df, pl):
    df.select(cols_bp12).filter(~pl.all_horizontal(pl.exclude("ID").is_null())).with_columns(
        pl.all().replace({-99: None, -88: None, 999: None})
    ).describe()
    return


@app.cell
def _(df, pb, pl):
    validation_bp12 = (
        pb.Validate(data=df)
        .col_vals_between(
            columns=pb.matches(r"^G\w{3}_BP12_2$"),
            left=48,
            right=195,
            na_pass=True,
            pre=lambda df: df.with_columns(
                pl.col(r"^G\w{3}_BP12_2$").replace({-99: None, -88: None, 999: None})
            ),
        )
        .col_vals_between(
            columns=pb.matches(r"^G\w{3}_BP13_2$"),
            left=20,
            right=144,
            na_pass=True,
            pre=lambda df: df.with_columns(
                pl.col(r"^G\w{3}_BP13_2$").replace({-99: None, -88: None, 999: None})
            ),
        )
        .col_vals_between(
            columns=pb.matches(r"^G\w{3}_BP14_2$"),
            left=29,
            right=166,
            na_pass=True,
            pre=lambda df: df.with_columns(
                pl.col(r"^G\w{3}_BP14_2$").replace({-99: None, -88: None})
            ),
        )
        .col_vals_between(
            columns=pb.matches(r"^G\w{3}_BP15_2$"),
            left=45,
            right=197,
            na_pass=True,
            pre=lambda df: df.with_columns(
                pl.col(r"^G\w{3}_BP15_2$").replace({-99: None, -88: None})
            ),
        )
        .col_vals_between(
            columns=pb.matches(r"^G\w{3}_BP16_2$"),
            left=19,
            right=158,
            na_pass=True,
            pre=lambda df: df.with_columns(
                pl.col(r"^G\w{3}_BP16_2$").replace({-99: None, -88: None})
            ),
        )
        .col_vals_between(
            columns=pb.matches(r"^G\w{3}_BP17_2$"),
            left=37,
            right=173,
            na_pass=True,
            pre=lambda df: df.with_columns(
                pl.col(r"^G\w{3}_BP17_2$").replace({-99: None, -88: None})
            ),
        )
        .col_vals_between(
            columns=pb.matches(r"^G\w{3}_BP18_2$"),
            left=33,
            right=229,
            na_pass=True,
            pre=lambda df: df.with_columns(
                pl.col(r"^G\w{3}_BP18_2$").replace({-99: None, -88: None})
            ),
        )
        .col_vals_between(
            columns=pb.matches(r"^G\w{3}_BP19_2$"),
            left=27,
            right=192,
            na_pass=True,
            pre=lambda df: df.with_columns(
                pl.col(r"^G\w{3}_BP19_2$").replace({-99: None, -88: None})
            ),
        )
        .col_vals_between(
            columns=pb.matches(r"^G\w{3}_BP20_2$"),
            left=45,
            right=186,
            na_pass=True,
            pre=lambda df: df.with_columns(
                pl.col(r"^G\w{3}_BP20_2$").replace({-99: None, -88: None})
            ),
        )
    ).interrogate()

    validation_bp12
    return


@app.cell
def _(mo):
    mo.md(r"""## G214 and G217 Exercise Variables""")
    return


@app.cell
def _(meta, pl):
    m_bp14 = meta.filter(pl.col("basename").str.contains(r"BP(14|17|20|64|65|66)$")).sort(
        by="basename"
    )
    cols_bp14 = m_bp14.to_series(0).to_list()
    m_bp14
    return (cols_bp14,)


@app.cell
def _(cols_bp14, df, pl):
    df.select(cols_bp14).filter(~pl.all_horizontal(pl.exclude("ID").is_null())).with_columns(
        pl.all().replace({-99: None, -88: None})
    ).describe()
    return


@app.cell
def _(df, pb, pl):
    validation_bp14 = (
        pb.Validate(data=df)
        .col_vals_between(
            columns=pb.matches(r"^G\w{3}_BP14$"),
            left=56,
            right=152,
            na_pass=True,
            pre=lambda df: df.with_columns(
                pl.col(r"^G\w{3}_BP14$").replace({-99: None, -88: None})
            ),
        )
        .col_vals_between(
            columns=pb.matches(r"^G\w{3}_BP17$"),
            left=46,
            right=173,
            na_pass=True,
            pre=lambda df: df.with_columns(
                pl.col(r"^G\w{3}_BP17$").replace({-99: None, -88: None})
            ),
        )
        .col_vals_between(
            columns=pb.matches(r"^G\w{3}_BP20$"),
            left=45,
            right=188,
            na_pass=True,
            pre=lambda df: df.with_columns(
                pl.col(r"^G\w{3}_BP20$").replace({-99: None, -88: None})
            ),
        )
        .col_vals_between(
            columns=pb.matches(r"^G\w{3}_BP64$"),
            left=58,
            right=199,
            na_pass=True,
            pre=lambda df: df.with_columns(
                pl.col(r"^G\w{3}_BP64$").replace({-99: None, -88: None})
            ),
        )
        .col_vals_between(
            columns=pb.matches(r"^G\w{3}_BP65$"),
            left=58,
            right=181,
            na_pass=True,
            pre=lambda df: df.with_columns(
                pl.col(r"^G\w{3}_BP65$").replace({-99: None, -88: None})
            ),
        )
        .col_vals_between(
            columns=pb.matches(r"^G\w{3}_BP66$"),
            left=52,
            right=189,
            na_pass=True,
            pre=lambda df: df.with_columns(
                pl.col(r"^G\w{3}_BP66$").replace({-99: None, -88: None})
            ),
        )
    ).interrogate()

    validation_bp14
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## Cycling Variables - `CYC[1-3]`""")
    return


@app.cell
def _(meta, pl):
    m_cyc = meta.filter(pl.col("basename").str.contains(r"CYC\d$")).sort(by="basename")
    cols_cyc = m_cyc.to_series(0).to_list()
    m_cyc
    return (cols_cyc,)


@app.cell
def _(cols_cyc, df, pl):
    df.select(cols_cyc).filter(~pl.all_horizontal(pl.exclude("ID").is_null())).with_columns(
        pl.all().replace({-99.0: None, 888.8: None, 999.9: None})
    ).describe()
    return


@app.cell
def _(df, pb, pl):
    validation_cyc = (
        pb.Validate(data=df)
        .col_vals_in_set(
            columns=pb.matches(r"^G\w{3}_CYC1$"),
            set=[12.5, 25.0, 50.0, 75.0, 100.0, None],
            pre=lambda df: df.with_columns(
                pl.col(r"^G\w{3}_CYC1$").replace({-99.0: None, 888.8: None, 999.9: None})
            ),
        )
        .col_vals_in_set(
            columns=pb.matches(r"^G\w{3}_CYC2$"),
            set=[12.5, 25.0, 37.5, 50.0, 62.5, 75.0, 87.5, 100.0, 125.0, 150.0, 175.0, 200.0, None],
            pre=lambda df: df.with_columns(
                pl.col(r"^G\w{3}_CYC2$").replace({-99.0: None, 888.8: None, 999.9: None})
            ),
        )
        .col_vals_in_set(
            columns=pb.matches(r"^G\w{3}_CYC3$"),
            set=[12.5, 25.0, 37.5, 50.0, 62.5, 75.0, 87.5, 100.0, 125.0, 150.0, 175.0, 200.0, None],
            pre=lambda df: df.with_columns(
                pl.col(r"^G\w{3}_CYC3$").replace({-99.0: None, 888.8: None, 999.9: None})
            ),
        )
    ).interrogate()

    validation_cyc
    return (validation_cyc,)


@app.cell
def _(pb, validation_cyc):
    validation_cyc.get_step_report(1, columns_subset=pb.matches("CYC"))
    return


@app.cell
def _(pb, validation_cyc):
    validation_cyc.get_step_report(2, columns_subset=pb.matches("CYC"))
    return


@app.cell
def _(pb, validation_cyc):
    validation_cyc.get_step_report(3, columns_subset=pb.matches("CYC"))
    return


@app.cell
def _(pb, validation_cyc):
    validation_cyc.get_step_report(4, columns_subset=pb.matches("CYC"))
    return


@app.cell
def _(pb, validation_cyc):
    validation_cyc.get_step_report(5, columns_subset=pb.matches("CYC"))
    return


@app.cell
def _(pb, validation_cyc):
    validation_cyc.get_step_report(6, columns_subset=pb.matches("ID|CYC"), limit=None)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## Miscellaneous Exercise Variables""")
    return


@app.cell
def _(meta, pl):
    m_misc = meta.filter(
        pl.col("basename").is_in(["PWC170", "TECH", "INST", "XCAR", "XCER_COM"])
    ).sort(by="basename")
    cols_misc = m_misc.to_series(0).to_list()
    m_misc
    return (cols_misc,)


@app.cell
def _(cols_misc, df, pl):
    df.select(cols_misc).filter(~pl.all_horizontal(pl.exclude("ID").is_null())).with_columns(
        pl.all().replace({-99: None, -88: None})
    ).describe()
    return


@app.cell
def _(df):
    # Investigate options for `G217_INST`
    df.select("G217_INST").unique()
    return


@app.cell
def _(df, pb, pl):
    pb.Validate(data=df).col_vals_between(
        columns=pb.matches(r"CYC\d"),
        left=12.5,
        right=400,
        na_pass=True,
        pre=lambda df: df.with_columns(pl.col(r"^G\w{3}_CYC\d$").replace({-99.0: None, -88.0: None, 888.8: None, 999.9: None})),
        segments=("G217_INST", pb.seg_group(["Dinamap 1", "Dinamap 2", "Dinamap 3", "Dinamap 4"]))
    ).col_vals_eq(
        columns=pb.matches(r"G217_CYC\d"),
        value=888.8,
        segments=("G217_INST", '        8')
    ).col_vals_null(
        columns=pb.matches(r"G217_CYC\d"),
        segments=("G217_INST", [None, ""])
    ).interrogate()
    return


@app.cell
def _(meta, pl):
    meta.filter(pl.col("Variable").str.contains("G214_BP"))
    return


@app.cell
def _(df, pl):
    df.select(pl.col("G214_XCAR", r"^G214_BP\d+$", "G214_PWC170")).filter(pl.col("G214_XCAR").eq(1))
    return


@app.cell
def _(df, pl):
    df.select("G214_XCAR", pl.col("^G214_BP.*$")).filter(pl.col("G214_XCAR").eq(0)).unique()
    return


@app.cell
def _(df, pl):
    df_bp = df.select("ID", "G214_XCAR", pl.col("^G214_BP(9|10|11|14|17|20|6[4-6]|2[1-3])$")).filter(~pl.all_horizontal(pl.exclude("ID").is_null()))
    df_bp
    return


@app.cell
def _(df, pb, pl):
    validation_misc = (
        pb.Validate(data=df).col_vals_between(
            columns=pb.matches(r"^G\w{3}_PWC170$"),
            left=25,
            right=344,
            na_pass=True,
            pre=lambda df: df.with_columns(pl.col(r"^G\w{3}_PWC170$").replace({-99: None})),
        )
        .col_vals_in_set(
            columns=pb.matches(r"^G\w{3}_TECH$"),
            set=[1, 2, 3, None],
            pre=lambda df: df.with_columns(pl.col(r"^G\w{3}_TECH$").replace({-99: None, -88: None})),
        )
    ).interrogate()

    validation_misc
    return


@app.cell
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
    validation_bp41 = (
        pb.Validate(data=df)
        .col_vals_between(
            columns=pb.matches(r"^G\w{3}_BP41$"),
            left=67,
            right=166,
            na_pass=True,
            pre=lambda df: df.with_columns(
                pl.col(r"^G\w{3}_BP41$").replace({-99: None, -88: None})
            ),
        )
        .col_vals_between(
            columns=pb.matches(r"^G\w{3}_BP42$"),
            left=34,
            right=97,
            na_pass=True,
            pre=lambda df: df.with_columns(
                pl.col(r"^G\w{3}_BP42$").replace({-99: None, -88: None})
            ),
        )
        .col_vals_between(
            columns=pb.matches(r"^G\w{3}_BP43$"),
            left=55,
            right=140,
            na_pass=True,
            pre=lambda df: df.with_columns(
                pl.col(r"^G\w{3}_BP43$").replace({-99: None, -88: None})
            ),
        )
        .col_vals_in_set(
            columns=pb.matches(r"^G\w{3}_BP44$"),
            set=[1, 2, None],
            pre=lambda df: df.with_columns(
                pl.col(r"^G\w{3}_BP44$").replace({-99: None, -88: None})
            ),
        )
    ).interrogate()

    validation_bp41
    return (validation_bp41,)


@app.cell
def _(pb, validation_bp41):
    validation_bp41.get_step_report(i=2, columns_subset=pb.matches("BP41"))
    return


if __name__ == "__main__":
    app.run()
