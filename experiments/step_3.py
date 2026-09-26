import torch
from torchvision import transforms, datasets
from torch.utils.data import DataLoader
from pathlib import Path

project_dir = Path(__file__).resolve().parents[1]
data_dir = project_dir / "Data" / "dementia_data_split"

train_dir = data_dir / "train"
test_dir = data_dir / "test"
val_dir = data_dir / "val"

# Define transformations for the training and testing sets

train_transforms = transforms.Compose([
    transforms.Grayscale(num_output_channels=1),  # Convert to grayscale
    transforms.Resize((224, 224)),  # Resize to 224x224
    transforms.ToTensor(),  # Convert to tensor
    transforms.Normalize(mean=[0.5], std=[0.5])  # Normalize
])

test_transforms = transforms.Compose([
    transforms.Grayscale(num_output_channels=1),  # Convert to grayscale 
    transforms.Resize((224, 224)),  # Resize to 224x224
    transforms.ToTensor(),  # Convert to tensor
    transforms.Normalize(mean=[0.5], std=[0.5])  # Normalize   
])

val_transforms = transforms.Compose([
    transforms.Grayscale(num_output_channels=1),  # Convert to grayscale 
    transforms.Resize((224, 224)),  # Resize to 224x224
    transforms.ToTensor(),  # Convert to tensor
    transforms.Normalize(mean=[0.5], std=[0.5])  # Normalize   
])

# Load the datasets with ImageFolder
train_dataset = datasets.ImageFolder(root=train_dir, transform=train_transforms)
test_dataset = datasets.ImageFolder(root=test_dir, transform=test_transforms)
val_dataset = datasets.ImageFolder(root=val_dir, transform=val_transforms)


#checking the class mapping
print("Class mapping:", train_dataset.class_to_idx)
print("Number of training samples:", len(train_dataset))
