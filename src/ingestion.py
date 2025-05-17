import pandas as pd

def load_raw_data(filepath):
    """Load raw data from a CSV file."""
    return pd.read_csv(filepath)

def clean_data(df):
    """Basic cleaning: drop duplicates and missing values."""
    df = df.drop_duplicates()
    df = df.dropna()
    return df

def ingest_and_clean(filepath):
    df = load_raw_data(filepath)
    df = clean_data(df)
    return df
