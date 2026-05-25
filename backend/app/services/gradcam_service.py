from ml.explainability import gradcam
from ml.explainability.gradcam import generate_gradcam


def create_gradcam(
        image_path : str,
):

    gradcam_path = generate_gradcam(image_path)

    return gradcam_path