from pydantic import BaseModel

class ChatRequest(
    BaseModel
):
    user_question: str
    prediction:str
    confidence:float