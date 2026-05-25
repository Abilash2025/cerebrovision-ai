from pathlib import Path

import matplotlib.pyplot as plt
import seaborn as sns
import torch
from sklearn.metrics import classification_report, confusion_matrix

from ml.datasets.brain_tumor_dataset import create_dataloaders
from ml.models.efficientnet_classifier import EfficientNetClassifier

#------Configuration------

DATA_DIR = "ml/data/raw/brain_tumor_mri_dataset"

CHECKPOINT_PATH = "ml/experiments/checkpoints/best_model.pth"

DEVICE = torch.device("cuda" if torch.cuda.is_available() else "cpu")

OUTPUT_DIR = Path("ml/experiments/evaluation")
OUTPUT_DIR.mkdir(exist_ok=True, parents=True)

#------Evaluation------

def evaluate_model():
    
    #Load Dataloaders
    _ , val_loader, class_names = create_dataloaders(DATA_DIR, )

    #Load Model
    model = EfficientNetClassifier(num_classes=len(class_names))
    model.load_state_dict(torch.load(CHECKPOINT_PATH, map_location=DEVICE))
    model.to(DEVICE)
    
    model.eval()

    all_predictions = []
    all_labels = []

    with torch.no_grad():
        for images, labels in val_loader:
            
            images, labels = images.to(DEVICE), labels.to(DEVICE)
            
            outputs = model(images)
            
            predictions = torch.argmax(outputs, dim=1)

            all_predictions.extend(predictions.cpu().numpy())
            all_labels.extend(labels.cpu().numpy())

    #Classification Report
    report = classification_report(all_labels, all_predictions, target_names=class_names)
    print("Classification Report:\n", report)

    #save report to file
    with open(OUTPUT_DIR / "classification_report.txt", "w") as f:  
        f.write(report)

    #Confusion Matrix
    cm = confusion_matrix(all_labels, all_predictions)
    plt.figure(figsize=(8, 6))

    sns.heatmap(cm, annot=True, fmt="d", cmap="Blues", xticklabels=class_names, yticklabels=class_names)
    plt.xlabel("Predicted Labels")
    plt.ylabel("True Label")
    plt.title("Confusion Matrix")
    plt.savefig(OUTPUT_DIR / "confusion_matrix.png")
    plt.show()

    plt.close()

    print(f"Confusion matrix saved to {OUTPUT_DIR / 'confusion_matrix.png'}")
    print(f"Classification report saved to {OUTPUT_DIR / 'classification_report.txt'}")

if __name__ == "__main__":
    evaluate_model()