import torch

from ml.models.efficientnet_classifier import EfficientNetClassifier

def main():
    model = EfficientNetClassifier(num_classes=4, dropout_rate=0.3)

    dummy_input = torch.randn(8, 3, 300, 300)

    outputs = model(dummy_input)

    print("Output shape:", outputs.shape)

if __name__ == "__main__":
    main()