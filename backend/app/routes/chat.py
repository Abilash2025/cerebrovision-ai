from fastapi import (
    APIRouter,
    HTTPException,
)

from backend.app.schemas.chat_schema import ChatRequest
from backend.app.services.chatbot_service import generate_chat_response

router = APIRouter()

@router.post("/chat")
async def chat(
    request: ChatRequest
):
    try:
        response = generate_chat_response(
            user_question=request.user_question,
            prediction=request.prediction,
            confidence=request.confidence,
        )

        return {
            "success" : True,
            "response": response,
        }
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e),
        )