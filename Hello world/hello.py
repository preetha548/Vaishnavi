import pandas as pd
from sklearn.tree import DecisionTreeClassifier

# Sample training data
data = {
    "communication": [9, 8, 3, 2, 7, 4, 9, 1, 6, 3],
    "trust":         [9, 8, 2, 3, 7, 4, 9, 2, 6, 3],
    "arguments":     [1, 2, 8, 7, 3, 6, 1, 9, 4, 7],
    "satisfaction":  [9, 8, 2, 3, 7, 4, 9, 1, 6, 3],
    "heartbreak":    [0, 0, 1, 1, 0, 1, 0, 1, 0, 1]
}

df = pd.DataFrame(data)

# Features and target
X = df[["communication", "trust", "arguments", "satisfaction"]]
y = df["heartbreak"]

# Train model
model = DecisionTreeClassifier(random_state=42)
model.fit(X, y)

# Get user's information
print("❤️ Heart Break Prediction")
print("-------------------------")

communication = int(input("Communication level (1-10): "))
trust = int(input("Trust level (1-10): "))
arguments = int(input("Arguments per week: "))
satisfaction = int(input("Relationship satisfaction (1-10): "))

# Prediction
prediction = model.predict([
    [communication, trust, arguments, satisfaction]
])[0]

if prediction == 1:
    print("\n💔 Prediction: Higher breakup risk")
else:
    print("\n❤️ Prediction: Lower breakup risk")
