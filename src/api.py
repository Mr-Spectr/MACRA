from flask import Flask, request, jsonify
import joblib
import pandas as pd
import os
import requests
import traceback

app = Flask(__name__)

MODEL_PATH = os.environ.get('MODEL_PATH', '../model.pkl')

# Load model at startup
model = None
if os.path.exists(MODEL_PATH):
    model = joblib.load(MODEL_PATH)

# Load metrics if available
def load_metrics():
    metrics_path = os.environ.get('METRICS_PATH', '../metrics.json')
    if os.path.exists(metrics_path):
        import json
        with open(metrics_path, 'r') as f:
            return json.load(f)
    return None

@app.route('/predict', methods=['POST'])
def predict():
    if model is None:
        return jsonify({'error': 'Model not loaded'}), 500
    data = request.get_json()
    if not data or 'features' not in data:
        return jsonify({'error': 'No features provided'}), 400
    try:
        features = pd.DataFrame([data['features']])
        # One-hot encode and align columns to model
        features = pd.get_dummies(features)
        for col in model.feature_names_in_:
            if col not in features.columns:
                features[col] = 0
        features = features[model.feature_names_in_]
        prediction = model.predict(features)
        # If regression, return float; if classification, return class
        pred_value = prediction.tolist()[0]
        return jsonify({'prediction': pred_value})
    except Exception as e:
        tb = traceback.format_exc()
        print('Prediction error:', tb)
        return jsonify({'error': str(e), 'traceback': tb}), 500

@app.route('/metrics', methods=['GET'])
def metrics():
    metrics = load_metrics()
    if metrics:
        return jsonify(metrics)
    else:
        return jsonify({'error': 'No metrics available'}), 404

@app.route('/')
def home():
    return 'MACRA API is running.'

LLM_API_URL = os.environ.get('LLM_API_URL', 'https://openrouter.ai/api/v1/chat/completions')
LLM_MODEL = os.environ.get('LLM_MODEL', 'deepseek/deepseek-r1:free')
LLM_API_KEY = os.environ.get('LLM_API_KEY', None)
LLM_REFERER = os.environ.get('LLM_REFERER', 'http://localhost')  # Set to your dashboard URL in prod
LLM_TITLE = os.environ.get('LLM_TITLE', 'MACRA Dashboard')

@app.route('/llm', methods=['POST'])
def llm():
    if not LLM_API_KEY:
        return jsonify({'error': 'No LLM API key set'}), 400
    data = request.get_json()
    prompt = data.get('prompt', '')
    if not prompt:
        return jsonify({'error': 'No prompt provided'}), 400
    headers = {
        'Authorization': f'Bearer {LLM_API_KEY}',
        'Content-Type': 'application/json',
        'HTTP-Referer': LLM_REFERER,
        'X-Title': LLM_TITLE
    }
    payload = {
        'model': LLM_MODEL,
        'messages': [
            {'role': 'user', 'content': prompt}
        ]
    }
    try:
        resp = requests.post(LLM_API_URL, headers=headers, json=payload, timeout=30)
        resp.raise_for_status()
        try:
            result = resp.json()
        except Exception:
            return jsonify({'error': 'Invalid JSON from LLM', 'raw': resp.text}), 502
        content = result.get('choices', [{}])[0].get('message', {}).get('content', '')
        return jsonify({'response': content})
    except Exception as e:
        tb = traceback.format_exc()
        return jsonify({'error': str(e), 'traceback': tb}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False, use_reloader=False)
