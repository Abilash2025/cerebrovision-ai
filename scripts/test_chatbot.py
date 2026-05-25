from backend.app.chatbot import generate_chat_response

from ml.vlm.report_generator import generate_radiology_report

def main():
    # Sample test case
    prediction = "glioma"
    confidence_score = 92.5
    user_question = "What does glioma mean?"

    report = generate_radiology_report(prediction, confidence_score)
    
    chatbot_response = generate_chat_response(
        user_question=user_question,
        prediction=prediction,
        confidence=confidence_score,
        report=report,
    )
    
    print("\n Chatbot Response:\n")
    print(chatbot_response)

if __name__ == "__main__":
    main()
    