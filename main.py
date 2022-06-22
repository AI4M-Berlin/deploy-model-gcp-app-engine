from typing import List

from fastapi import FastAPI
from google.cloud import aiplatform


app = FastAPI()
endpoint = aiplatform.Endpoint(
    endpoint_name="3582296844224430080",
    project="ai4medicine-cloud",
    location="europe-west3"
)

@app.get("/")
def home():
    return {"message": "Hello world"}

@app.post("/prediction/")
def call_prediction(patient: List[float]):
    prediction = endpoint.predict(instances=[patient])
    return {
        "prediction": prediction.predictions[0],
        "model_id": prediction.deployed_model_id
        }
