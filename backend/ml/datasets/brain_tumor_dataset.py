from pathlib import Path

import torch
from torchvision import datasets, transforms
from torch.utils.data import DataLoader

IMAGE_SIZE = 300
BATCH_SIZE = 32
NUM_WORKERS = 2

def get_train_transforms():
    """
    Training transformations with light augmentation.

    These augmentations help improve model generalization
    while remaining medically reasonable for MRI images.
    """
    return transforms.Compose([
        transforms.Resize((IMAGE_SIZE, IMAGE_SIZE)),
        transforms.RandomHorizontalFlip(p=0.5),
        transforms.RandomRotation(degrees=10),
        transforms.ToTensor(),
        transforms.Normalize(
            mean=[0.485, 0.456, 0.406], 
            std=[0.229, 0.224, 0.225]
        )
    ])

def get_validation_transforms():
    """
    Validation transformations without augmentation.

    Only resizing and normalization to ensure consistent input size
    and pixel value distribution for evaluation.
    """
    return transforms.Compose([
        transforms.Resize((IMAGE_SIZE, IMAGE_SIZE)),
        transforms.ToTensor(),
        transforms.Normalize(
            mean=[0.485, 0.456, 0.406], 
            std=[0.229, 0.224, 0.225]
        )
    ])

def create_dataloaders(data_dir:str):
    """
    Create DataLoaders for training and validation datasets.

    Args:
        data_dir (str): Path to the dataset directory containing 'train' and 'val' subdirectories.
    Returns:
        Tuple[DataLoader, DataLoader, List[str]]: Training and validation DataLoaders and class names.
    """

    data_path = Path(data_dir)

    train_dataset = datasets.ImageFolder(
        root=data_path / "Training",
        transform=get_train_transforms(),
    )

    val_dataset = datasets.ImageFolder(
        root=data_path / "Testing",
        transform=get_validation_transforms(),
    )

    train_loader = DataLoader(
        dataset=train_dataset,
        batch_size=BATCH_SIZE,
        shuffle=True,
        num_workers=NUM_WORKERS,
        pin_memory=True,
    )

    val_loader = DataLoader(
        dataset=val_dataset,
        batch_size=BATCH_SIZE,
        shuffle=False,
        num_workers=NUM_WORKERS,
        pin_memory=True,
    )

    class_names = train_dataset.classes

    return train_loader, val_loader, class_names
