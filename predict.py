from src.components.data_ingestion import DataIngestion
from src.pipelines.prediction_pipeline import PredictionPipeline

ingestion = DataIngestion()

_, valid_df = ingestion.load_data()

sample = valid_df.drop(
    columns=["sales"]
).head()

pipeline = PredictionPipeline()

prediction = pipeline.predict(sample)

print(prediction)

