from ml.vlm.report_generator import (
    generate_radiology_report
)

def create_report(
    prediction: str,
    confidence: float,
):

    report = generate_radiology_report(
        prediction=prediction,
        confidence=confidence,
    )

    return report