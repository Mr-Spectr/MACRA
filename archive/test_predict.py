# Legacy ML test script archived on 2025-05-17 after LLM migration.
# Original contents preserved for reference.
import joblib
import pandas as pd

model = joblib.load('model.pkl')
print('Model loaded:', type(model))
print('Model expects:', model.feature_names_in_)

row = {'country':'Afghanistan','countryCode':'AFG','Year':2000,'gdpGrowth':2.5,'unemployment':8.1}
df = pd.DataFrame([row])
df = pd.get_dummies(df)
for col in model.feature_names_in_:
    if col not in df.columns:
        df[col] = 0
df = df[model.feature_names_in_]
pred = model.predict(df)
print('Prediction:', pred)
