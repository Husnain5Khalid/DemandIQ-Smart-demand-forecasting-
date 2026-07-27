import pandas as pd
import sys

from demand_iq.logger import logger
from demand_iq.exception import DemandIQException
from demand_iq.config import PROCESSED_DATA_DIR


class DataIngestion:
    """
    Loads processed datasets for model training.
    """

    def __init__(self):

        self.train_path = PROCESSED_DATA_DIR / "train_data.csv"

        self.valid_path = PROCESSED_DATA_DIR / "valid_data.csv"

    def load_data(self):

        try:

            logger.info("Loading processed datasets.")

            train_df = pd.read_csv(self.train_path)

            valid_df = pd.read_csv(self.valid_path)

            logger.info("Datasets loaded successfully.")

            return train_df, valid_df

        except Exception as e:

            logger.error("Failed to load processed datasets.")

            raise DemandIQException(e, sys)