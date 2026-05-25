from pathlib import Path

import torch
from PIL import Image
from torchvision import transforms

from ml.models.efficientnet_classifier import EfficientNetClassifier

#----Configurations----#

IMAGE_SIZE = 300

CLASS_NAMES = [
        "glioma",
    "meningioma",
    "notumor",
    "pituitary",
]

CHECKPOINT_PATH = "ml/experiments/checkpoints/best_model.pth"

DEVICE = torch.device("cuda" if torch.cuda.is_available() else "cpu")

#----Image Preprocessing----#

inference_transforms = transforms.Compose([
    transforms.Resize((IMAGE_SIZE, IMAGE_SIZE)),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], 
                         std=[0.229, 0.224, 0.225]),
])

#----Model Loading----#

def model_load():

    model = EfficientNetClassifier(num_classes=len(CLASS_NAMES))
    model.load_state_dict(torch.load(CHECKPOINT_PATH, map_location=DEVICE,))
    model.to(DEVICE)
    model.eval()
    return model

#----Prediction Function----#

def predict_image(image_path:str):

    print("Loading TensorFlow model...")
    
    model = model_load()

    image = Image.open(image_path).convert("RGB")

    image_tensor = inference_transforms(image)

    #Add Batch Dimension
    image_tensor = image_tensor.unsqueeze(0).to(DEVICE)

    with torch.no_grad():
        outputs = model(image_tensor)

        probabilities = torch.softmax(outputs, dim=1,)

        confidence, predicted_class = torch.max(probabilities, dim=1)

    predicted_label = CLASS_NAMES[predicted_class.item()]
    confidence_score = confidence.item()

    return {
        "predicted_label": predicted_label,
        "confidence_score": round(confidence_score * 100, 2)
    }
