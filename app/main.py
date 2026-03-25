# training script
from fastapi import FastAPI
import joblib

app = FastAPI()

# Load trained model
model = joblib.load("model.pkl")

@app.get("/")
def home():
    return {"message": "Churn Prediction API is running"}

@app.post("/predict")
def predict(feature1: float, feature2: float):
    data = [[feature1, feature2]]
    prediction = model.predict(data)
    
    return {
        "prediction": int(prediction[0])
    }
uvicorn app.main:app --reload
