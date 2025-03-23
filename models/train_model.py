import pickle
from sklearn.linear_model import LogisticRegression

# Dummy data
X_train = [[0], [1], [2], [3], [4]]
y_train = [0, 1, 1, 0, 1]

model = LogisticRegression()
model.fit(X_train, y_train)

with open("model.pkl", "wb") as f:
    pickle.dump(model, f)

print("Model trained and saved.")
