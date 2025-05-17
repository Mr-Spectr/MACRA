import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from pymongo import MongoClient

def load_data_from_mongodb(uri, db_name, collection_name, query={}):
    client = MongoClient(uri)
    db = client[db_name]
    collection = db[collection_name]
    data = list(collection.find(query))
    if data and '_id' in data[0]:
        for row in data:
            row.pop('_id', None)
    df = pd.DataFrame(data)
    return df

def load_json_data(filepath):
    """Load data from a JSON file."""
    return pd.read_json(filepath)

def load_data(filepath):
    """Load data from CSV or JSON based on file extension."""
    if filepath.endswith('.json'):
        return load_json_data(filepath)
    else:
        return pd.read_csv(filepath)

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