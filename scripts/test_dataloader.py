from ml.datasets.brain_tumor_dataset import create_dataloaders

DATA_DIR = "ml/data/raw/brain_tumor_mri_dataset"

def main():
    train_loader, val_loader, class_names = create_dataloaders(DATA_DIR)

    print(f"class names: {class_names}")

    images, labels = next(iter(train_loader))

    print(f"Image batch shape: {images.shape}")
    print(f"Label batch shape: {labels.shape}")

if __name__ == "__main__":
    main()