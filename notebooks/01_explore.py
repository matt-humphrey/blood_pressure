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
    bp10 = df.select("ID", pl.col(r"^G\w{3}_BP10$")).filter(
        ~pl.all_horizontal(pl.exclude("ID").is_null())
    )
    bp10
    return (bp10,)


@app.cell
def _(bp10):
    bp10.describe()
    return


@app.cell
def _(bp10, pl):
    bp10.select(pl.exclude("ID")).with_columns(
        pl.col(r"^G\w{3}_BP10$").replace({-99: None, -88: None})
    ).describe()
    return


@app.cell
def _(df, pb, pl):
    validation_bp10 = (
        pb.Validate(data=df).col_vals_between(
            columns=pb.matches(r"^G\w{3}_BP10$"),
            left=30,
            right=114,
            na_pass=True,
            pre=lambda df: df.with_columns(
                pl.col(r"^G\w{3}_BP10$").replace({-99: None, -88: None})
            ),
        )
    ).interrogate()

    validation_bp10
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## BP11""")
    return


@app.cell
def _(meta, pl):
    meta.filter(pl.col("basename").eq("BP11"))
    return


@app.cell
def _(df, pl):
    bp11 = df.select("ID", pl.col(r"^G\w{3}_BP11$")).filter(
        ~pl.all_horizontal(pl.exclude("ID").is_null())
    )
    bp11
    return (bp11,)


@app.cell
def _(bp11):
    bp11.describe()
    return


@app.cell
def _(bp11, pl):
    bp11.select(pl.exclude("ID")).with_columns(
        pl.col(r"^G\w{3}_BP11$").replace({-99: None, -88: None})
    ).describe()
    return


@app.cell
def _(df, pb, pl):
    validation_bp11 = (
        pb.Validate(data=df).col_vals_between(
            columns=pb.matches(r"^G\w{3}_BP11$"),
            left=45,
            right=137,
            na_pass=True,
            pre=lambda df: df.with_columns(
                pl.col(r"^G\w{3}_BP11$").replace({-99: None, -88: None})
            ),
        )
    ).interrogate()

    validation_bp11
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ## `G208_BP12_2` and `G21[47]_BP_14`

    For the exercise/cycle ergometer variables, there are discrepancies that may not be harmonisable.
    For Y8, increments were 1.5 minutes, whereas for Y14 and Y17, they were 1 minute increments.
    """
    )
    return


@app.cell
def _(meta, pl):
    meta.filter(pl.col("basename").is_in(["BP12_2", "BP14"]))
    return


@app.cell
def _(df, pl):
    bp12 = df.select("ID", pl.col(r"^G\w{3}_BP(12_2|14)$")).filter(
        ~pl.all_horizontal(pl.exclude("ID").is_null())
    )
    bp12
    return (bp12,)


@app.cell
def _(bp12):
    bp12.describe()
    return


@app.cell
def _(bp12, pl):
    bp12.select(pl.exclude("ID")).with_columns(
        pl.col(r"^G\w{3}_BP(12_2|14)$").replace({-99: None, -88: None, 999: None})
    ).describe()
    return


@app.cell
def _(df, pb, pl):
    validation_bp12 = (
        pb.Validate(data=df).col_vals_between(
            columns=pb.matches(r"^G\w{3}_BP(12_2|14)$"),
            left=48,
            right=195,
            na_pass=True,
            pre=lambda df: df.with_columns(
                pl.col(r"^G\w{3}_BP(12_2|14)$").replace({-99: None, -88: None, 999: None})
            ),
        )
    ).interrogate()

    validation_bp12
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## `BP21`""")
    return


@app.cell
def _(meta, pl):
    meta.filter(pl.col("basename").is_in(["BP21"]))
    return


@app.cell
def _(df, pl):
    bp21 = df.select("ID", pl.col(r"^G\w{3}_BP21$")).filter(
        ~pl.all_horizontal(pl.exclude("ID").is_null())
    )
    bp21
    return (bp21,)


@app.cell
def _(bp21):
    bp21.describe()
    return


@app.cell
def _(bp21, pl):
    bp21.select(pl.exclude("ID")).with_columns(
        pl.col(r"^G\w{3}_BP21$").replace({-99: None, -88: None})
    ).describe()
    return


@app.cell
def _(df, pb, pl):
    validation_bp21 = (
        pb.Validate(data=df).col_vals_between(
            columns=pb.matches(r"^G\w{3}_BP21$"),
            left=68,
            right=217,
            na_pass=True,
            pre=lambda df: df.with_columns(
                pl.col(r"^G\w{3}_BP21$").replace({-99: None, -88: None})
            ),
        )
    ).interrogate()

    validation_bp21
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## `BP22`, `BP23` and `BP24`""")
    return


@app.cell
def _(meta, pl):
    meta.filter(pl.col("basename").is_in(["BP22", "BP23", "BP24"])).sort(by="basename")
    return


@app.cell
def _(df, pl):
    bp22 = df.select("ID", pl.col(r"^G\w{3}_BP2[2-4]$")).filter(
        ~pl.all_horizontal(pl.exclude("ID").is_null())
    )
    return (bp22,)


@app.cell
def _(bp22, pl):
    bp22.select(pl.exclude("ID")).with_columns(
        pl.col(r"^G\w{3}_BP2[2-4]$").replace(
            {-99: None, -88: None}
        )  # -99: None, -88: None, 999: None
    ).describe()
    return


@app.cell
def _(df, pb, pl):
    validation_bp22 = (
        pb.Validate(data=df)
        .col_vals_between(
            columns=pb.matches(r"^G\w{3}_BP22$"),
            left=31,
            right=128,
            na_pass=True,
            pre=lambda df: df.with_columns(
                pl.col(r"^G\w{3}_BP22$").replace({-99: None, -88: None})
            ),
        )
        .col_vals_between(
            columns=pb.matches(r"^G\w{3}_BP23$"),
            left=51,
            right=173,
            na_pass=True,
            pre=lambda df: df.with_columns(
                pl.col(r"^G\w{3}_BP23$").replace({-99: None, -88: None})
            ),
        )
        .col_vals_in_set(
            columns=pb.matches(r"^G\w{3}_BP24$"),
            set=[1, 2, None],
            pre=lambda df: df.with_columns(
                pl.col(r"^G\w{3}_BP24$").replace({-99: None, -88: None})
            ),
        )
    ).interrogate()

    validation_bp22
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## `BP25`, `BP26`, `BP27` and `BP28`""")
    return


@app.cell
def _(meta, pl):
    meta.filter(pl.col("basename").is_in(["BP25", "BP26", "BP27", "BP28"])).sort(by="basename")
    return


@app.cell
def _(df, pl):
    df.select(pl.col(r"^G\w{3}_BP2[5-8]$")).filter(
        ~pl.all_horizontal(pl.exclude("ID").is_null())
    ).with_columns(pl.all().replace({-99: None, -88: None})).describe()
    return


@app.cell
def _(df, pb, pl):
    validation_bp25 = (
        pb.Validate(data=df)
        .col_vals_between(
            columns=pb.matches(r"^G\w{3}_BP25$"),
            left=68,
            right=213,
            na_pass=True,
            pre=lambda df: df.with_columns(
                pl.col(r"^G\w{3}_BP25$").replace({-99: None, -88: None})
            ),
        )
        .col_vals_between(
            columns=pb.matches(r"^G\w{3}_BP26$"),
            left=33,
            right=119,
            na_pass=True,
            pre=lambda df: df.with_columns(
                pl.col(r"^G\w{3}_BP26$").replace({-99: None, -88: None})
            ),
        )
        .col_vals_between(
            columns=pb.matches(r"^G\w{3}_BP27$"),
            left=49,
            right=153,
            na_pass=True,
            pre=lambda df: df.with_columns(
                pl.col(r"^G\w{3}_BP27$").replace({-99: None, -88: None})
            ),
        )
        .col_vals_in_set(
            columns=pb.matches(r"^G\w{3}_BP28$"),
            set=[1, 2, None],
            pre=lambda df: df.with_columns(
                pl.col(r"^G\w{3}_BP28$").replace({-99: None, -88: None})
            ),
        )
    ).interrogate()

    validation_bp25
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## `BP29`, `BP30`, `BP31` and `BP32`""")
    return


@app.cell
def _(meta, pl):
    m29 = meta.filter(pl.col("basename").is_in(["BP29", "BP30", "BP31", "BP32"])).sort(
        by="basename"
    )
    cols29 = m29.to_series(0).to_list()
    m29
    return (cols29,)


@app.cell
def _(cols29, df, pl):
    df.select(cols29).filter(~pl.all_horizontal(pl.exclude("ID").is_null())).with_columns(
        pl.all().replace({-99: None, -88: None})
    ).describe()
    return


@app.cell
def _(df, pb, pl):
    validation_bp29 = (
        pb.Validate(data=df)
        .col_vals_between(
            columns=pb.matches(r"^G\w{3}_BP29$"),
            left=61,
            right=186,
            na_pass=True,
            pre=lambda df: df.with_columns(
                pl.col(r"^G\w{3}_BP29$").replace({-99: None, -88: None})
            ),
        )
        .col_vals_between(
            columns=pb.matches(r"^G\w{3}_BP30$"),
            left=32,
            right=108,
            na_pass=True,
            pre=lambda df: df.with_columns(
                pl.col(r"^G\w{3}_BP30$").replace({-99: None, -88: None})
            ),
        )
        .col_vals_between(
            columns=pb.matches(r"^G\w{3}_BP31$"),
            left=47,
            right=148,
            na_pass=True,
            pre=lambda df: df.with_columns(
                pl.col(r"^G\w{3}_BP31$").replace({-99: None, -88: None})
            ),
        )
        .col_vals_in_set(
            columns=pb.matches(r"^G\w{3}_BP32$"),
            set=[1, 2, None],
            pre=lambda df: df.with_columns(
                pl.col(r"^G\w{3}_BP32$").replace({-99: None, -88: None})
            ),
        )
    ).interrogate()

    validation_bp29
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## `BP33`, `BP34`, `BP35` and `BP36`""")
    return


@app.cell
def _(meta, pl):
    m33 = meta.filter(pl.col("basename").is_in(["BP33", "BP34", "BP35", "BP36"])).sort(
        by="basename"
    )
    cols33 = m33.to_series(0).to_list()
    m33
    return (cols33,)


@app.cell
def _(cols33, df, pl):
    df.select(cols33).filter(~pl.all_horizontal(pl.exclude("ID").is_null())).with_columns(
        pl.all().replace({-99: None, -88: None})
    ).describe()
    return


@app.cell
def _(df, pb, pl):
    validation_bp33 = (
        pb.Validate(data=df)
        .col_vals_between(
            columns=pb.matches(r"^G\w{3}_BP33$"),
            left=79,
            right=183,
            na_pass=True,
            pre=lambda df: df.with_columns(
                pl.col(r"^G\w{3}_BP33$").replace({-99: None, -88: None})
            ),
        )
        .col_vals_between(
            columns=pb.matches(r"^G\w{3}_BP34$"),
            left=31,
            right=102,
            na_pass=True,
            pre=lambda df: df.with_columns(
                pl.col(r"^G\w{3}_BP34$").replace({-99: None, -88: None})
            ),
        )
        .col_vals_between(
            columns=pb.matches(r"^G\w{3}_BP35$"),
            left=46,
            right=137,
            na_pass=True,
            pre=lambda df: df.with_columns(
                pl.col(r"^G\w{3}_BP35$").replace({-99: None, -88: None})
            ),
        )
        .col_vals_in_set(
            columns=pb.matches(r"^G\w{3}_BP36$"),
            set=[1, 2, None],
            pre=lambda df: df.with_columns(
                pl.col(r"^G\w{3}_BP36$").replace({-99: None, -88: None})
            ),
        )
    ).interrogate()

    validation_bp33
    return


@app.cell
def _(mo):
    mo.md(r"""## `BP37`, `BP38`, `BP39` and `BP40`""")
    return


@app.cell
def _(meta, pl):
    m37 = meta.filter(pl.col("basename").is_in(["BP37", "BP38", "BP39", "BP40"])).sort(
        by="basename"
    )
    cols37 = m37.to_series(0).to_list()
    m37
    return (cols37,)


@app.cell
def _(cols37, df, pl):
    df.select(cols37).filter(~pl.all_horizontal(pl.exclude("ID").is_null())).with_columns(
        pl.all().replace({-99: None, -88: None})
    ).describe()
    return


@app.cell
def _(df, pb, pl):
    validation_bp37 = (
        pb.Validate(data=df)
        .col_vals_between(
            columns=pb.matches(r"^G\w{3}_BP37$"),
            left=53,
            right=177,
            na_pass=True,
            pre=lambda df: df.with_columns(
                pl.col(r"^G\w{3}_BP37$").replace({-99: None, -88: None})
            ),
        )
        .col_vals_between(
            columns=pb.matches(r"^G\w{3}_BP38$"),
            left=27,
            right=100,
            na_pass=True,
            pre=lambda df: df.with_columns(
                pl.col(r"^G\w{3}_BP38$").replace({-99: None, -88: None})
            ),
        )
        .col_vals_between(
            columns=pb.matches(r"^G\w{3}_BP39$"),
            left=50,
            right=142,
            na_pass=True,
            pre=lambda df: df.with_columns(
                pl.col(r"^G\w{3}_BP39$").replace({-99: None, -88: None})
            ),
        )
        .col_vals_in_set(
            columns=pb.matches(r"^G\w{3}_BP40$"),
            set=[1, 2, None],
            pre=lambda df: df.with_columns(
                pl.col(r"^G\w{3}_BP40$").replace({-99: None, -88: None})
            ),
        )
    ).interrogate()

    validation_bp37
    return


@app.cell
def _(mo):
    mo.md(r"""## `BP41`, `BP42`, `BP43` and `BP44`""")
    return


@app.cell
def _(meta, pl):
    m41 = meta.filter(pl.col("basename").is_in(["BP41", "BP42", "BP43", "BP44"])).sort(
        by="basename"
    )
    cols41 = m41.to_series(0).to_list()
    m41
    return (cols41,)


@app.cell
def _(cols41, df, pl):
    df.select(cols41).filter(~pl.all_horizontal(pl.exclude("ID").is_null())).with_columns(
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
