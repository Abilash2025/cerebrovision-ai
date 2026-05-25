from ml.inference.predict import predict_image

IMAGE_PATH = "ml/data/raw/brain_tumor_mri_dataset/Testing/pituitary/Te-pi_5.jpg"

def main():
    result = predict_image(IMAGE_PATH)

    print("Prediction Result:   \n")

    print(result)

if __name__ == "__main__":
    main()