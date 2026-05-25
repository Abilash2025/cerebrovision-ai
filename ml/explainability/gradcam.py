from pathlib import Path

import cv2
import matplotlib.pyplot as plt
import numpy as np
import torch
from PIL import Image
from pytorch_grad_cam import GradCAM
from pytorch_grad_cam.utils.image import show_cam_on_image,preprocess_image

from ml.models.efficientnet_classifier import EfficientNetClassifier

#----Configurations----#

CLASS_NAMES = [
        "glioma",
        "meningioma",
        "notumor",
        "pituitary",
]

IMG_SIZE = 300

CHECKPOIT_PATH = "ml/experiments/checkpoints/best_model.pth"

DEVICE = torch.device("cuda" if torch.cuda.is_available() else "cpu")

OUTPUT_DIR = Path("ml/experiments/gradcam")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

#----Model Loading----#

def model_load():
    model = EfficientNetClassifier(num_classes=len(CLASS_NAMES))
    model.load_state_dict(torch.load(CHECKPOIT_PATH, map_location=DEVICE,))
    model.to(DEVICE)
    model.eval()
    return model

#----Grad-CAM Generation----#

def generate_gradcam(image_path:str):
    
    model = model_load()

    #Load Image
    image = Image.open(image_path).convert("RGB")
    image = image.resize((IMG_SIZE, IMG_SIZE))
    rgb_image = np.array(image).astype(np.float32) / 255.0
    input_tensor = preprocess_image(rgb_image, mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225],)
    input_tensor = input_tensor.to(DEVICE)

    #Target Layer for Grad-CAM
    target_layers = [model.backbone.conv_head]

    cam = GradCAM(model=model, target_layers=target_layers,)

    grayscale_cam = cam(input_tensor=input_tensor)[0]

    visulaization = show_cam_on_image(rgb_image, grayscale_cam, use_rgb=True)

    output_path = OUTPUT_DIR / f"{Path(image_path).stem}_gradcam.jpg"
    cv2.imwrite(str(output_path), cv2.cvtColor(visulaization, cv2.COLOR_RGB2BGR),)

    
    
    #Plotting the Grad-CAM
    plt.figure(figsize=(8, 8))
    plt.imshow(visulaization)
    plt.axis("off")
    plt.title(f"Grad-CAM Visualization")
    
    # Backend visualization must save files only and not display them, 
    # so the following code is commented out.
    # plt.show()

    plt.savefig(output_path)
    plt.close()
    
    print(f"Grad-CAM saved at: {output_path}")

    return output_path