from flask import Flask, request, jsonify
import joblib
import pandas as pd
import os

app = Flask(__name__)

MODEL_PATH = os.environ.get('MODEL_PATH', 'model.pkl')

# Load model at startup
model = None
if os.path.exists(MODEL_PATH):
    model = joblib.load(MODEL_PATH)

@app.route('/predict', methods=['POST'])
def predict():
    if model is None:
        return jsonify({'error': 'Model not loaded'}), 500
    data = request.get_json()
    if not data or 'features' not in data:
        return jsonify({'error': 'No features provided'}), 400
    features = pd.DataFrame([data['features']])
    prediction = model.predict(features)
    return jsonify({'prediction': prediction.tolist()})

@app.route('/')
def home():
    return 'MACRA API is running.'

if __name__ == '__main__':
    app.run(debug=True)
