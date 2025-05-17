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
    from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor
    from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, mean_squared_error, r2_score
    from data_preprocessing import load_data
    import sys

    # Load data from JSON file
    data = load_data('../data/final_data.json')  # Update path if needed
    # Automatically detect the target column as the last column
    target_column = data.columns[-1]
    # Drop rows where the target is NaN
    data = data.dropna(subset=[target_column])
    X = data.drop(target_column, axis=1)
    y = data[target_column]

    # One-hot encode categorical features
    X = pd.get_dummies(X)

    # Split the data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Check if target is continuous (regression) or categorical (classification)
    if pd.api.types.is_numeric_dtype(y) and y.nunique() > 20:
        print(f"Detected continuous target column '{target_column}'. Using RandomForestRegressor.")
        model = RandomForestRegressor()
        trained_model = train_model(X_train, y_train, model, '../model.pkl')
        print(f"Model trained and saved as '../model.pkl'. Target column used: {target_column}")
        # Regression evaluation
        y_pred = trained_model.predict(X_test)
        mse = mean_squared_error(y_test, y_pred)
        r2 = r2_score(y_test, y_pred)
        print(f"\nRegression Model Evaluation on Test Set:")
        print(f"MSE:  {mse:.4f}")
        print(f"R2:   {r2:.4f}")
        # Save metrics
        metrics = {
            'type': 'regression',
            'target_column': str(target_column),
            'mse': mse,
            'r2': r2
        }
    else:
        print(f"Detected categorical target column '{target_column}'. Using RandomForestClassifier.")
        model = RandomForestClassifier()
        trained_model = train_model(X_train, y_train, model, '../model.pkl')
        print(f"Model trained and saved as '../model.pkl'. Target column used: {target_column}")
        # Classification evaluation
        y_pred = trained_model.predict(X_test)
        accuracy = accuracy_score(y_test, y_pred)
        precision = precision_score(y_test, y_pred, average='weighted', zero_division=0)
        recall = recall_score(y_test, y_pred, average='weighted', zero_division=0)
        f1 = f1_score(y_test, y_pred, average='weighted', zero_division=0)
        print(f"\nClassification Model Evaluation on Test Set:")
        print(f"Accuracy:  {accuracy:.4f}")
        print(f"Precision: {precision:.4f}")
        print(f"Recall:    {recall:.4f}")
        print(f"F1 Score:  {f1:.4f}")
        # Save metrics
        metrics = {
            'type': 'classification',
            'target_column': str(target_column),
            'accuracy': accuracy,
            'precision': precision,
            'recall': recall,
            'f1': f1
        }
    # Save metrics to file
    import json
    with open('../metrics.json', 'w') as f:
        json.dump(metrics, f, indent=2)

if __name__ == "__main__":
    main()