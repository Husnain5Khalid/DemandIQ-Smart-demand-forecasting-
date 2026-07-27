import pandas as pd

from demand_iq.pipelines.prediction_pipeline import PredictionPipeline

pipeline = PredictionPipeline()


def predict(data: dict):

    df = pd.DataFrame([data])

    prediction = pipeline.predict(df)

    return float(prediction[0])