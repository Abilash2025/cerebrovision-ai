from sre_constants import SUCCESS

from fastapi import APIRouter
from sympy import true

from app.utils.file_utils import cleanup_files

router = APIRouter()

@router.post("/cleanup")
async def cleanup_cache(
    paths: list[str]
):
    cleanup_files(*paths)

    return {
        "success" : True
    }