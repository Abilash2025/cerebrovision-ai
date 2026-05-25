from ml.explainability.gradcam import generate_gradcam

IMAGE_PATH = "ml/data/raw/brain_tumor_mri_dataset/Testing/pituitary/Te-pi_5.jpg"

def main():
    generate_gradcam(IMAGE_PATH)

if __name__ == "__main__":
    main()

    