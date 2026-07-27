from src.components.data_ingestion import DataIngestion
from src.components.data_transformation import DataTransformation

# Load data
ingestion = DataIngestion()
train_df, valid_df = ingestion.load_data()

# Transform data
transformer = DataTransformation()

(
    X_train_processed,
    y_train,
    X_valid_processed,
    y_valid,
    preprocessor
) = transformer.transform_data(
    train_df,
    valid_df
)

from src.components.model_trainner import ModelTrainer

trainer = ModelTrainer()

model, metrics = trainer.train(
    X_train_processed,
    y_train,
    X_valid_processed,
    y_valid
)

print(metrics)

