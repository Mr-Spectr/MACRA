import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

def load_data(filepath):
    data = pd.read_csv(filepath)
    return data

def clean_data(data):
    # Example cleaning steps
    data = data.dropna()  # Remove missing values
    data = data[data['column_name'] != 'unwanted_value']  # Remove unwanted values
    return data

def preprocess_data(filepath):
    data = load_data(filepath)
    data = clean_data(data)
    
    # Normalize features
    features = data.drop('target_column', axis=1)
    target = data['target_column']
    
    scaler = StandardScaler()
    features_scaled = scaler.fit_transform(features)
    
    return train_test_split(features_scaled, target, test_size=0.2, random_state=42)