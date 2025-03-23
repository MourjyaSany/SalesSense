import pickle
import numpy as np
import pandas as pd

# Load the trained AI model
with open("models/model.pkl", "rb") as f:
    model = pickle.load(f)

# Define function to score a lead
def score_lead(data):
    try:
        # Convert input data into a DataFrame with the correct column order
        df = pd.DataFrame([data], columns=["age", "income", "website_visits", "email_clicks"])
        
        # Predict lead score (probability of conversion)
        score = model.predict_proba(df)[0][1] * 100  # Convert to percentage
        
        return round(score, 2)  # Return lead score rounded to 2 decimal places
    except Exception as e:
        return f"Error in scoring: {str(e)}"
