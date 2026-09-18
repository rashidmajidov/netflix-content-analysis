import pandas as pd
from src.config import DATA_RAW, DATA_PROCESSED

def load_raw(filename: str) -> pd.DataFrame:
    return pd.read_csv(DATA_RAW / filename)

def save_processed(df: pd.DataFrame, filename: str) -> None:
    df.to_csv(DATA_PROCESSED / filename, index=False)

def load_processed(filename: str) -> pd.DataFrame:
    return pd.read_csv(DATA_PROCESSED / filename)