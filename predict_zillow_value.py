import joblib
import numpy as np
import pandas as pd

pipeline = joblib.load("model/zillow_pipeline.pkl")

feature_names = ['bedroomcnt', 'bathroomcnt', 'calculatedfinishedsquarefeet', 'lotsizesquarefeet', 'floors', 'regionidzip']

def predict_home_value(features):
    input_df = pd.DataFrame([features], columns=feature_names)
    prediction = pipeline.predict(input_df)
    return float(prediction[0])
