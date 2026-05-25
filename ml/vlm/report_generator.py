from datetime import datetime


def generate_radiology_report(
    prediction: str,
    confidence: float,
):

    confidence_level = (
        "Very High"
        if confidence >= 95
        else "High"
        if confidence >= 85
        else "Moderate"
        if confidence >= 75
        else "Low"
    )

    findings_map = {
        "glioma":
            "Imaging findings suggest the presence of a glioma-like abnormality within the brain MRI scan.",

        "meningioma":
            "Imaging findings are consistent with a meningioma-like lesion observed in the brain MRI scan.",

        "pituitary":
            "MRI findings indicate features associated with a pituitary tumor-like abnormality.",

        "notumor":
            "No significant tumor-related abnormality detected within the analyzed MRI scan.",
    }

    return {

        "exam_information": {
            "modality":
                "Brain MRI",

            "analysis_type":
                "AI-Assisted Tumor Classification",

            "generated_on":
                datetime.now().strftime(
                    "%Y-%m-%d %H:%M:%S"
                ),
        },

        "clinical_context":
            (
                "The uploaded brain MRI scan "
                "was analyzed using a "
                "deep learning-based "
                "brain tumor classification "
                "system with explainability support."
            ),

        "imaging_technique":
            (
                "MRI scan analyzed using "
                "Convolutional Neural Networks "
                "(CNN) and Grad-CAM "
                "visual explainability."
            ),

        "findings":
            findings_map.get(
                prediction.lower(),
                "No significant findings."
            ),

        "impression":
            (
                f"The AI system predicts "
                f"a {prediction.upper()} "
                f"classification with "
                f"{confidence_level.lower()} "
                f"confidence."
            ),

        "confidence_assessment": {
            "prediction":
                prediction.upper(),

            "confidence_score":
                f"{confidence}%",

            "confidence_level":
                confidence_level,
        },

        "recommendations":
            (
                "Clinical correlation and "
                "professional radiological "
                "evaluation are strongly "
                "recommended."
            ),

        "disclaimer":
            (
                "CerebroVision AI is an "
                "experimental educational "
                "system and should not "
                "be used as a substitute "
                "for professional medical diagnosis."
            ),
    }