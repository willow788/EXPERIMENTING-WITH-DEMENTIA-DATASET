#now we will really look at the brain images from each class

from PIL import Image
import os
import matplotlib.pyplot as plt

for class_name in ["Mild Dementia", "Moderate Dementia", "Non Demented", "Very mild Dementia"]:

    #define the path to the class directory
    class_path = os.path.join("Data", class_name)

    img_files = [
        f for f in os.listdir(class_path) if f.endswith(".jpg")

        
    ]

    #image path
    img_path = os.path.join(class_path, img_files[0])

    image = Image.open(img_path)

    plt.imshow(image)
    plt.title(f"Class: {class_name}, Image: {img_files[0]}")
    plt.axis('off')
    plt.savefig(f"brain_images_{class_name.replace(' ', '_')}.png")
    
    plt.show()
    