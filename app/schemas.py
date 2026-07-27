from pydantic import BaseModel
from typing import Any


class PredictionRequest(BaseModel):
    data: dict[str, Any]

    