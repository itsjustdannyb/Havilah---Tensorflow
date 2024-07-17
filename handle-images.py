import os
from PIL import Image
import numpy as np

path = r"C:\Users\danie\OneDrive\Documents\Datasets\dog-breed-images\dataset"

def show_paths(path, size=(250,250)):
    images = [] # numerical
    labels = []
    dog_breeds = os.listdir(path)

    for dog_breed in dog_breeds:
        dog_folder = os.path.join(path, dog_breed)
        if not os.path.isdir(dog_folder):
            continue

        for dog in os.listdir(dog_folder):
            img_path = os.path.join(dog_folder, dog)
            img = Image.open(img_path).convert("RGB") # make image RGB
            # img = img.resize(size, Image.ANTIALIAS) #antialias tries to retain image quality when resized
            img = img.resize(size, Image.Resampling.LANCZOS) #Image.Resampling.LANCZOS updated version of Image.ANIALIAS

            img_array = np.array(img) # height, width and channels

            images.append(img_array)
            labels.append(dog_breed)

    images = np.array(images)
    labels = np.array(labels)

    return images, labels

X, y = show_paths(path)

print(X.shape)
print(y.shape)
print(X)
print(y)