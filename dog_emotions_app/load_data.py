import os
import pandas as pd
from torchvision.io import read_image

"""
How to split it if the label is as a folder name? 
Should I download each folder separately and label it?
It would look like image - name - label
"""

class DogImageSet(Dataset):
    def __init__(self, annotations_file, img_dir, transform=None, target_transform=None):
        self.img_labels = pd.read_csv(annotations_file)
        self.img_dir = img_dir
        self.transform = transform
        self.targer_transform = target_transform

    def __len__(self):
        return len(self.img_labels) 

    def __getitem__(self, idx):
        img_path = os.path.join(self.img_dir, self.img_labels.iloc[idx, 0])
        image = read_image(img_path)
        label = self.img_labels.iloc[idx, 1]
        if self.transform:
            image = self.transform(image)
        if self.targer_transform:
            label = self.targer_transform(label)
        return image, label
