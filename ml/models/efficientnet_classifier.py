"""Defines the model architecture for the EfficientNet classifier."""

import torch
import torch.nn as nn
import timm

class EfficientNetClassifier(nn.Module):
    """
        Efficientnet- B3 based brain tumor classifier.

        This model uses transfer learning from ImageNet-pretrained
        EfficientNet weights and replaces the original classification
        head with a custom tumor classification head.
    """

    def __init__(
            self,
            num_classes: int = 4,
            dropout_rate: float = 0.3,
    ):
        super().__init__()

        # Load the EfficientNet-B3 model with pretrained weights
        self.backbone = timm.create_model(
            'efficientnet_b3',
            pretrained=True,
        )

        #Get input feature size of the classifier
        in_features = self.backbone.classifier.in_features

        #Replace original classifier head 
        self.backbone.classifier = nn.Sequential(
            nn.Dropout(p=dropout_rate),
            nn.Linear(in_features, num_classes)
        )
    
    def forward(self, x: torch.Tensor) -> torch.Tensor:
        """
            Forward pass through the model.

            Args:
                x (torch.Tensor): Input tensor of shape (batch_size, 3, H, W)

            Returns:
                torch.Tensor: Output logits of shape (batch_size, num_classes)
        """
        return self.backbone(x)