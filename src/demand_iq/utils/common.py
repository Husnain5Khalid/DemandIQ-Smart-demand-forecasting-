import json
import joblib
import sys

from pathlib import Path

from demand_iq.logger import logger
from demand_iq.exception import DemandIQException


def save_object(file_path: Path, obj) -> None:
    """
    Save any Python object using joblib.

    Parameters
    ----------
    file_path : Path
        Destination path.
    obj : Any
        Python object to save.
    """
    try:
        file_path.parent.mkdir(parents=True, exist_ok=True)

        joblib.dump(obj, file_path)

        logger.info(f"Object saved successfully at: {file_path}")

    except Exception as e:
        logger.exception("Failed to save object.")

        raise DemandIQException(e, sys)


def load_object(file_path: Path):
    """
    Load a Python object using joblib.

    Parameters
    ----------
    file_path : Path
        Path of saved object.

    Returns
    -------
    Any
        Loaded Python object.
    """
    try:
        logger.info(f"Loading object from: {file_path}")

        obj = joblib.load(file_path)

        logger.info("Object loaded successfully.")

        return obj

    except Exception as e:
        logger.exception("Failed to load object.")

        raise DemandIQException(e, sys)


def save_json(file_path: Path, data: dict) -> None:
    """
    Save dictionary as JSON.

    Parameters
    ----------
    file_path : Path
        JSON file path.
    data : dict
        Dictionary to save.
    """
    try:
        file_path.parent.mkdir(parents=True, exist_ok=True)

        with open(file_path, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)

        logger.info(f"JSON saved successfully at: {file_path}")

    except Exception as e:
        logger.exception("Failed to save JSON.")

        raise DemandIQException(e, sys)


def load_json(file_path: Path) -> dict:
    """
    Load JSON file.

    Parameters
    ----------
    file_path : Path
        JSON file path.

    Returns
    -------
    dict
        Loaded dictionary.
    """
    try:
        logger.info(f"Loading JSON from: {file_path}")

        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)

        logger.info("JSON loaded successfully.")

        return data

    except Exception as e:
        logger.exception("Failed to load JSON.")

        raise DemandIQException(e, sys)