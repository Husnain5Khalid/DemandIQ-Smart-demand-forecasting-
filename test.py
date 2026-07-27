from src.components.data_ingestion import DataIngestion

ingestion = DataIngestion()

train_df, valid_df = ingestion.load_data()

print(train_df.shape)

print(valid_df.shape)