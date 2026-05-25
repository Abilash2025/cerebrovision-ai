from fastapi import APIRouter, BackgroundTasks, HTTPException
from fastapi.responses import StreamingResponse

from backend.app.schemas.pdf_schema import PDFRequest
from backend.app.services.pdf_service import (
    generate_pdf_report
)
from backend.app.utils.file_utils import cleanup_files

router = APIRouter()


@router.post("/generate-pdf")
async def generate_pdf(
    request: PDFRequest,
):

    try:
        print(request)
        pdf_buffer = generate_pdf_report(
                prediction=
                    request.prediction,

                confidence=
                    request.confidence,

                report_sections=
                    request.report_sections,

                original_mri_path=
                    request.original_mri_path,

                gradcam_local_path=
                    request.gradcam_local_path,
            )

        return StreamingResponse(
            pdf_buffer,
            media_type=
                "application/pdf",

            headers={
                "Content-Disposition":
                    "attachment; filename=cerebrovision_report.pdf"
            },
        )

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )