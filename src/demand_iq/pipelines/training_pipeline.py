from demand_iq.logger import logger
from demand_iq.exception import DemandIQException

from src.components.data_ingestion import DataIngestion
from src.components.data_transformation import DataTransformation
from src.components.model_trainner import ModelTrainer

import sys


class TrainingPipeline:
    """
    Complete training workflow.
    """

    def run_pipeline(self):

        try:

            logger.info("=" * 70)
            logger.info("TRAINING PIPELINE STARTED")
            logger.info("=" * 70)

            ####################################
            # Data Ingestion
            ####################################

            ingestion = DataIngestion()

            train_df, valid_df = ingestion.load_data()

            logger.info("Data Ingestion Completed.")

            ####################################
            # Data Transformation
            ####################################

            transformation = DataTransformation()

            (
                X_train,
                y_train,
                X_valid,
                y_valid,
                preprocessor

            ) = transformation.transform_data(
                train_df,
                valid_df
            )

            logger.info("Data Transformation Completed.")

            ####################################
            # Model Training
            ####################################

            trainer = ModelTrainer()

            model, metrics = trainer.train(
                X_train,
                y_train,
                X_valid,
                y_valid
            )

            logger.info("Model Training Completed.")

            logger.info("=" * 70)
            logger.info("TRAINING PIPELINE FINISHED")
            logger.info("=" * 70)

            return model, metrics

        except Exception as e:

            logger.error("Training Pipeline Failed.")

            raise DemandIQException(
                e,
                sys
            )