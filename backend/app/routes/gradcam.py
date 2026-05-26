from pathlib import Path
from fastapi import (
    APIRouter,
    UploadFile,
    File,
    Request
)
from sympy import true

from app.routes.predict import UPLOAD_DIR
from app.services.gradcam_service import create_gradcam


router = APIRouter()

UPLOAD_DIR = Path("tmp/uploads")
UPLOAD_DIR.mkdir(
    exist_ok=True,
    parents=True,
)

@router.post("/gradcam")
async def gradcam(
    request: Request,
    file : UploadFile = File(...)
):
    file_path = (
        UPLOAD_DIR / file.filename
    )

    with open(
        file_path,
        "wb",
    ) as buffer:
        buffer.write(
            await file.read()
        )

    gradcam_path = create_gradcam(str(file_path))

    base_url = str(request.base_url)
    gradcam_url = (f"{base_url}static/gradcam/{Path(gradcam_path).name}")

    gradcam_local_path = str(Path(gradcam_path.resolve()))

    return {
        "success" : True,
        "gradcam_url" : gradcam_url,
        "gradcam_local_path":gradcam_local_path,
    }