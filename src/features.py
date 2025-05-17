import pandas as pd
from sklearn.preprocessing import StandardScaler

def engineer_features(df):
    """Example feature engineering: scale all numeric columns except target."""
    features = df.select_dtypes(include=['float64', 'int64']).columns.tolist()
    if 'target' in features:
        features.remove('target')
    scaler = StandardScaler()
    df[features] = scaler.fit_transform(df[features])
    return df
