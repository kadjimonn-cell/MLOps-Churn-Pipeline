#training script for school project
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib

# Step 1: Create simple sample data (since no dataset provided)
data = pd.DataFrame({
    "feature1": [1, 2, 3, 4, 5, 6],
    "feature2": [10, 20, 30, 40, 50, 60],
    "churn":    [0, 0, 1, 0, 1, 1]
})

# Step 2: Split features and target
X = data[["feature1", "feature2"]]
y = data["churn"]

# Step 3: Train model
model = RandomForestClassifier()
model.fit(X, y)

# Step 4: Save model
joblib.dump(model, "model.pkl")

print("✅ Model trained and saved as model.pkl")
