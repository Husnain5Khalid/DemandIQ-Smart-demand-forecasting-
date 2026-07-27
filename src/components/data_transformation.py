import sys

from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder

from demand_iq.logger import logger
from demand_iq.exception import DemandIQException
from demand_iq.config import PREPROCESSOR_PATH
from demand_iq.utils.common import save_object


class DataTransformation:

    def __init__(self):

        self.target = "sales"

        self.drop_columns = ["date"]

    def transform_data(
        self,
        train_df,
        valid_df
    ):

        try:

            logger.info("Starting data transformation.")

            X_train = train_df.drop(
                columns=[self.target]
            )

            y_train = train_df[self.target]

            X_valid = valid_df.drop(
                columns=[self.target]
            )

            y_valid = valid_df[self.target]

            X_train = X_train.drop(
                columns=self.drop_columns,
                errors="ignore"
            )

            X_valid = X_valid.drop(
                columns=self.drop_columns,
                errors="ignore"
            )

            categorical_columns = X_train.select_dtypes(
                include=["object"]
            ).columns.tolist()

            preprocessor = ColumnTransformer(
                transformers=[
                    (
                        "categorical",
                        OneHotEncoder(
                            handle_unknown="ignore"
                        ),
                        categorical_columns
                    )
                ],
                remainder="passthrough"
            )

            X_train_processed = preprocessor.fit_transform(
                X_train
            )

            X_valid_processed = preprocessor.transform(
                X_valid
            )

            save_object(
                PREPROCESSOR_PATH,
                preprocessor
            )

            logger.info(
                "Data transformation completed."
            )

            return (
                X_train_processed,
                y_train,
                X_valid_processed,
                y_valid,
                preprocessor
            )

        except Exception as e:

            logger.error(
                "Data transformation failed."
            )

            raise DemandIQException(
                e,
                sys
            )

        