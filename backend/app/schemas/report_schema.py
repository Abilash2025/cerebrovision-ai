from pydantic import BaseModel


class ReportRequest(
    BaseModel
):
    prediction: str
    confidence: float