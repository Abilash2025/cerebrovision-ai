from ml.inference.predict import predict_image

def run_prediction(
        image_path: str
):
    
    result = predict_image(image_path)

    return result