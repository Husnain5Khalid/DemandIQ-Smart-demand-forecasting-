import sys
import time

import numpy as np
import lightgbm as lgb

from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score,
)

from demand_iq.logger import logger
from demand_iq.exception import DemandIQException
from demand_iq.config import (
    MODEL_PATH,
    METRICS_PATH,
    RANDOM_STATE,
)
from demand_iq.utils.common import (
    save_object,
    save_json,
)


class ModelTrainer:
    """
    Train, evaluate and save the machine learning model.
    """

    def __init__(self):

        self.model = lgb.LGBMRegressor(
            random_state=RANDOM_STATE,
            verbose=-1
        )

    def evaluate(self, y_true, y_pred):
        """
        Calculate evaluation metrics.
        """

        mae = mean_absolute_error(
            y_true,
            y_pred
        )

        rmse = np.sqrt(
            mean_squared_error(
                y_true,
                y_pred
            )
        )

        r2 = r2_score(
            y_true,
            y_pred
        )

        wape = (
            np.sum(np.abs(y_true - y_pred))
            /
            np.sum(np.abs(y_true))
        )

        smape = np.mean(
            (
                2 * np.abs(y_true - y_pred)
            )
            /
            (
                np.abs(y_true)
                +
                np.abs(y_pred)
                +
                1e-10
            )
        ) * 100

        return {
            "MAE": round(float(mae), 4),
            "RMSE": round(float(rmse), 4),
            "R2": round(float(r2), 4),
            "WAPE": round(float(wape), 4),
            "SMAPE": round(float(smape), 4),
        }

    def train(
        self,
        X_train,
        y_train,
        X_valid,
        y_valid,
    ):
        """
        Train LightGBM model and evaluate it.
        """

        try:

            logger.info("=" * 60)
            logger.info("MODEL TRAINING STARTED")
            logger.info("=" * 60)

            start_time = time.time()

            logger.info("Training LightGBM model...")

            self.model.fit(
                X_train,
                y_train
            )

            logger.info("Model training completed.")

            logger.info("Generating predictions...")

            predictions = self.model.predict(
                X_valid
            )

            logger.info("Calculating evaluation metrics...")

            metrics = self.evaluate(
                y_valid,
                predictions
            )

            metrics["Training_Time"] = round(
                time.time() - start_time,
                2
            )

            logger.info("Saving trained model...")

            save_object(
                MODEL_PATH,
                self.model
            )

            logger.info("Saving evaluation metrics...")

            save_json(
                METRICS_PATH,
                metrics
            )

            logger.info("=" * 60)
            logger.info("MODEL TRAINING COMPLETED")
            logger.info("=" * 60)

            return self.model, metrics

        except Exception as e:

            logger.error("Model training failed.")

            raise DemandIQException(
                e,
                sys
            )