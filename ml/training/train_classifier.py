from pathlib import Path

import torch
from torch import nn
from torch.optim import Adam
from tqdm import tqdm

from ml.datasets.brain_tumor_dataset import create_dataloaders
from ml.models.efficientnet_classifier import EfficientNetClassifier

#--------Congiguration--------

DATA_DIR = "ml/data/raw/brain_tumor_mri_dataset"

BATCH_SIZE = 32
LEARNING_RATE = 1e-4
NUM_EPOCHS = 10

DEVICE = torch.device("cuda" if torch.cuda.is_available() else "cpu")

CHECKPOINT_DIR = Path("ml/experiments/checkpoints")
CHECKPOINT_DIR.mkdir(parents=True, exist_ok=True)


#--------Training Loop--------
def train_one_epoch(model, dataloader, criterion, optimizer):
    """
        Runs one epoch of training.
        Args:
            model: The neural network model to train.
            dataloader: DataLoader providing the training data.
            criterion: Loss function to optimize.
            optimizer: Optimization algorithm for updating model weights.

        Returns:
            tuple: (epoch_loss, epoch_accuracy)

    """
    model.train()
    running_loss = 0.0
    correct_predictions = 0
    total_samples = 0

    progress_bar = tqdm(dataloader, desc="Training")
    
    for images, labels in progress_bar:
        images, labels = images.to(DEVICE), labels.to(DEVICE)

        optimizer.zero_grad()

        outputs = model(images)
        loss = criterion(outputs, labels)
        loss.backward()
        optimizer.step()

        running_loss += loss.item() 
        predictions = torch.argmax(outputs, dim=1)
        correct_predictions += (predictions == labels).sum().item()
        total_samples += labels.size(0)

        accuracy = correct_predictions / total_samples

        progress_bar.set_postfix(
            loss=loss.item(),
            accuracy=f"{accuracy:.4f}"
        )

    epoch_loss = running_loss / len(dataloader)
    epoch_accuracy = correct_predictions / total_samples

    return epoch_loss, epoch_accuracy


#--------Validation Loop--------

def validate(model, dataloader, criterion):
    """
        Runs validation on the provided dataloader.

        Args:
            model: The neural network model to validate.
            dataloader: DataLoader providing the validation data.
            criterion: Loss function to evaluate.

        Returns:
            tuple: (validation_loss, validation_accuracy)
    """

    model.eval()

    running_loss = 0.0
    correct_predictions = 0
    total_samples = 0

    with torch.no_grad():
        for images, labels in tqdm(dataloader, desc="Validation"):
            images, labels = images.to(DEVICE), labels.to(DEVICE)

            outputs = model(images)
            loss = criterion(outputs, labels)

            running_loss += loss.item() 
            predictions = torch.argmax(outputs, dim=1)
            correct_predictions += (predictions == labels).sum().item()
            total_samples += labels.size(0)
    
    epoch_loss = running_loss / len(dataloader)
    epoch_accuracy = correct_predictions / total_samples

    return epoch_loss, epoch_accuracy



#--------Main Training Function--------

def main():

    print(f"using device: {DEVICE}")

    train_loader, val_loader, class_names = create_dataloaders(DATA_DIR)

    print(f"classes: {class_names}")

    model = EfficientNetClassifier(num_classes=len(class_names)).to(DEVICE)

    criterion = nn.CrossEntropyLoss()
    optimizer = Adam(model.parameters(), lr=LEARNING_RATE)

    best_val_accuracy = 0.0

    for epoch in range(NUM_EPOCHS):

        print(f"Epoch {epoch+1}/{NUM_EPOCHS}")

        train_loss, train_accuracy = train_one_epoch(model, train_loader, criterion, optimizer)

        val_loss, val_accuracy = validate(model, val_loader, criterion)

        print(f"Train Loss: {train_loss:.4f} | " 
              f"Train Accuracy: {train_accuracy:.4f}")
        
        print(f"Val Loss: {val_loss:.4f} | "
              f"Val Accuracy: {val_accuracy:.4f}")

        #save best model checkpoint
        if val_accuracy > best_val_accuracy:
            best_val_accuracy = val_accuracy
            checkpoint_path = CHECKPOINT_DIR / f"best_model.pth"
            torch.save(model.state_dict(), checkpoint_path,)
            print(f"Saved new best model checkpoint to {checkpoint_path}")

if __name__ == "__main__":
    main()
