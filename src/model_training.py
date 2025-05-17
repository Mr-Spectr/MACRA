def train_model(X_train, y_train, model, save_path):
    model.fit(X_train, y_train)
    import joblib
    joblib.dump(model, save_path)
    return model

def load_model(model_path):
    import joblib
    return joblib.load(model_path)

def main():
    import pandas as pd
    from sklearn.model_selection import train_test_split
    from sklearn.ensemble import RandomForestClassifier  # Example model
    from data_preprocessing import load_data_from_mongodb

    # MongoDB connection details
    uri = "mongodb://localhost:27017/"
    db_name = "your_db"
    collection_name = "your_collection"

    # Load data from MongoDB
    data = load_data_from_mongodb(uri, db_name, collection_name)
    X = data.drop('target_column', axis=1)  # Replace with your actual target column
    y = data['target_column']               # Replace with your actual target column
    # Split the data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train the model
    model = RandomForestClassifier()  # Example model
    trained_model = train_model(X_train, y_train, model, 'path/to/save/model.pkl')  # Update with actual path

if __name__ == "__main__":
    main()