from fastapi import APIRouter, HTTPException

from backend.app.schemas.report_schema import ReportRequest
from backend.app.services.report_service import create_report

router = APIRouter()

@router.post("/generate-report")
async def generate_report(
    request: ReportRequest
):
    try:
        report_sections = create_report(
            prediction=request.prediction,
            confidence=request.confidence,
        )

        return {
            "success" : True,
            "report_sections": report_sections,
        }
    
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )