from pathlib import Path

def getting_no_of_imgs():
    data_dir = Path(__file__).resolve().parent.parent / "Data"

    classes = [
    "Mild Dementia",
    "Moderate Dementia",
    "Non Demented",
    "Very mild Dementia"
    ]

    for class_name in classes:
        class_path = data_dir / class_name
        image_cnt = 0
        Mild_dementia = 0
        moderate_dementia = 0
        very_mild_dementia = 0
        non_demented = 0
        if class_name == "Mild Dementia":
            Mild_dementia += 1
        elif class_name == "Moderate Dementia":
            moderate_dementia += 1
        elif class_name == "Very mild Dementia":
            very_mild_dementia += 1
        elif class_name == "Non Demented":
            non_demented += 1

        # Count the number of images in the class directory
        for image_file in class_path.glob("*.jpg"):
            image_cnt += 1
            

        #printing the number of images in the class
        print(f"Class: {class_name}, Number of images: {image_cnt}")




if __name__ == "__main__":
    getting_no_of_imgs()
        
