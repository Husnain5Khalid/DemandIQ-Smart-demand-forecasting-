from fastapi import FastAPI

from app.schemas import PredictionRequest
from app.predictor import predict

app = FastAPI(
    title="Demand IQ API",
    version="1.0.0"
)


@app.get("/")
def home():

    return {
        "message": "Demand IQ API is running."
    }


@app.post("/predict")
def make_prediction(request: PredictionRequest):

    prediction = predict(request.data)

    return {
        "prediction": prediction
    }