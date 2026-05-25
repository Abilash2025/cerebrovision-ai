from pathlib import Path

from fastapi import (
    APIRouter,
    UploadFile,
    File
)
from sympy import true

from backend.app.services.prediction_service import run_prediction

router = APIRouter()

UPLOAD_DIR = Path("backend/uploads")
UPLOAD_DIR.mkdir(
    exist_ok=True,
    parents=True
)

@router.post("/predict")
async def predict(
    file: UploadFile = File(...)
):
    
    file_path = UPLOAD_DIR/ file.filename

    with open(file_path, "wb") as buffer:
        buffer.write(await file.read())

    result = run_prediction(str(file_path))

    return {
        "success" : True,
        "result" : result,
        "image_path": str(file_path.resolve()),
    }

