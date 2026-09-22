import os
import random
import shutil
from pathlib import Path

#setting a random seed for reproducibility
random.seed(42)

#specifying the data directory
data_dir = Path(__file__).resolve().parent.parent / "Data"
split_dir = data_dir / "dementia_data_split"

classes = [
    "Mild Dementia",
    "Moderate Dementia",
    "Non Demented",
    "Very mild Dementia"
]


#using a 80-10-10 split for training, validation, and testing
for split in ["train", "val", "test"]:
    for class_name in classes:
        (split_dir / split / class_name).mkdir(parents=True, exist_ok=True)


for class_name in classes:

    class_path = data_dir / class_name
    img_files = [f for f in os.listdir(class_path) if f.endswith(".jpg")]

    #shuffling the images to ensure randomness
    random.shuffle(img_files)

    #calculating the number of images for each split
    total_images = len(img_files)
    train_count = int(0.8 * total_images)
    val_count = int(0.1 * total_images)
    test_count = total_images - train_count - val_count

    #splitting the images into train, validation, and test sets
    train_imgs = img_files[:train_count]
    val_imgs = img_files[train_count:train_count + val_count]
    test_imgs = img_files[train_count + val_count:]

    #moving the images to their respective directories
    for img in train_imgs:
        shutil.move(str(class_path / img), str(split_dir / "train" / class_name / img))

    for img in val_imgs:
        shutil.move(str(class_path / img), str(split_dir / "val" / class_name / img))

    for img in test_imgs:
        shutil.move(str(class_path / img), str(split_dir / "test" / class_name / img))