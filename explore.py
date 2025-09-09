import pointblank as pb
import polars as pl

from blood_pressure import read_all_datasets
from blood_pressure.config import DATASETS

df, meta = read_all_datasets(DATASETS)

meta["basename"].unique().sort()

bp10 = df.select(pl.col(r"^G\w{3}_BP10$")).filter(~pl.any_horizontal(pl.all().is_null()))

bp10.describe()

bp10.with_columns(pl.col(r"^G\w{3}_BP10$").replace({-99: None, -88: None})).describe()

pb.Validate(data=bp10).col_vals_between(columns="G208_BP10", left=30, right=108).interrogate()
