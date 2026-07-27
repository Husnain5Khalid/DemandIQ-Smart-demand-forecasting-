import pandas as pd

from demand_iq.config import (
    MODEL_PATH,
    PREPROCESSOR_PATH
)

from demand_iq.logger import logger
from demand_iq.exception import DemandIQException

from demand_iq.utils.common import load_object

import sys

import sys

import pandas as pd

from demand_iq.config import (
    MODEL_PATH,
    PREPROCESSOR_PATH
)

from demand_iq.logger import logger
from demand_iq.exception import DemandIQException

from demand_iq.utils.common import load_object


class PredictionPipeline:

    def __init__(self):

        logger.info("Loading trained model.")

        self.model = load_object(
            MODEL_PATH
        )

        logger.info("Loading preprocessor.")

        self.preprocessor = load_object(
            PREPROCESSOR_PATH
        )

    def predict(
        self,
        data: pd.DataFrame
    ):

        try:

            logger.info(
                "Generating predictions."
            )

            data = data.drop(
                columns=["date"],
                errors="ignore"
            )

            transformed = self.preprocessor.transform(
                data
            )

            prediction = self.model.predict(
                transformed
            )

            logger.info(
                "Prediction completed."
            )

            return prediction

        except Exception as e:

            logger.error(
                "Prediction failed."
            )

            raise DemandIQException(
                e,
                sys
            )