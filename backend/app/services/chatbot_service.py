import google.generativeai as genai

from backend.app.core.config import GEMINI_API_KEY, MODEL

genai.configure(
    api_key=GEMINI_API_KEY
)

def generate_chat_response(
    user_question: str,
    prediction: str,
    confidence: float,
):

    prompt = f"""
    You are CerebroVision AI, an educational medical imaging assistant.

    MRI Prediction:
    {prediction}

    Confidence:
    {confidence}%

    User Question:
    {user_question}

    Instructions:
    - Answer ONLY the user's question directly.
    - Keep responses concise and easy to understand.
    - Avoid unnecessary medical details unless specifically asked.
    - Use a calm and professional tone.
    - Reference the MRI prediction only when relevant.
    - Do not provide definitive diagnosis.
    - Do not overwhelm the user with long explanations.
    - Encourage consulting a medical professional when appropriate.
    """
    
    model = genai.GenerativeModel(
        MODEL
    )

    response = model.generate_content(
        prompt
    )

    return response.text