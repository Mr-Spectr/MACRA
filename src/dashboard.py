import streamlit as st
import pandas as pd
import requests

st.title('MACRA - Market Credibility Risk Analyzer Dashboard')

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
                results.append(response.json()['prediction'][0])
            else:
                results.append('error')
        df['Prediction'] = results
        st.write('Prediction Results:')
        st.dataframe(df)
