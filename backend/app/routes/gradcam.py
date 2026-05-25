from hashlib import file_digest
from pathlib import Path
from fastapi import (
    APIRouter,
    UploadFile,
    File
)
from sympy import true

from backend.app.routes.predict import UPLOAD_DIR
from backend.app.services.gradcam_service import create_gradcam


router = APIRouter()

UPLOAD_DIR = Path("backend/uploads")
UPLOAD_DIR.mkdir(
    exist_ok=True,
    parents=True,
)

@router.post("/gradcam")
async def gradcam(
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

    return {
        "success" : True,
        "gradcam_url" : f"http://127.0.0.1:8000/static/gradcam/{Path(gradcam_path).name}",
        "gradcam_local_path":str(
                                    Path(gradcam_path.resolve())
                                ),
    }