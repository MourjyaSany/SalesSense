import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

# Load dataset
df = pd.read_csv("models/leads_data.csv")

# Ensure all required features are used
X = df[["age", "income", "website_visits", "email_clicks"]]  # Select the correct features
y = df["purchase_made"]  # Target variable

# Train/Test Split (80% train, 20% test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = LogisticRegression()
model.fit(X_train, y_train)

# Save trained model
with open("models/model.pkl", "wb") as f:
    pickle.dump(model, f)

print("✅ Model trained successfully with features:", X.columns.tolist())
