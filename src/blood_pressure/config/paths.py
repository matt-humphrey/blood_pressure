from pathlib import Path

PROJECT_ROOT = Path(__file__).parents[3]

DATA = PROJECT_ROOT / "data"
OG_DATA = DATA / "0 original"
RAW_DATA = DATA / "1 raw"
INTERIM_DATA = DATA / "2 interim"
PROCESSED_DATA = DATA / "3 processed"
