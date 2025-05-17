import streamlit as st
import pandas as pd
import requests

st.title('MACRA - Market Credibility Risk Analyzer Dashboard')

# Show model evaluation metrics
st.header('Model Evaluation Metrics')
try:
    metrics = requests.get('http://localhost:5000/metrics').json()
    if 'error' not in metrics:
        for k, v in metrics.items():
            st.write(f"**{k.capitalize()}**: {v}")
    else:
        st.warning(metrics['error'])
except Exception as e:
    st.warning(f"Could not fetch metrics: {e}")

st.write('Upload a CSV file with the same features as the model expects:')
uploaded_file = st.file_uploader('Choose a CSV file', type='csv')

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write('Data Preview:')
    st.dataframe(df.head())
    if st.button('Predict Market Credibility'):
        api_url = 'http://localhost:5000/predict'
        results = []
        for _, row in df.iterrows():
            response = requests.post(api_url, json={'features': row.to_dict()})
            if response.ok:
                results.append(response.json()['prediction'])
            else:
                results.append('error')
        df['Prediction'] = results
        st.write('Prediction Results:')
        st.dataframe(df)

st.header('LLM Chat (Deepseek/Gemini/OpenAI)')
llm_prompt = st.text_area('Enter your prompt for the LLM:')
if st.button('Ask LLM'):
    api_url = 'http://localhost:5000/llm'
    try:
        resp = requests.post(api_url, json={'prompt': llm_prompt}, timeout=30)
        if resp.ok:
            try:
                st.success(resp.json().get('response', 'No response'))
            except Exception as e:
                st.error(f"Invalid JSON response: {resp.text}")
        else:
            st.error(f"API error: {resp.status_code} - {resp.text}")
    except Exception as e:
        st.error(f'LLM request failed: {e}')
