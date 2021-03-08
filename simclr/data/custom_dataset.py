import numpy as np
import torch
from torch.utils.data import Dataset
from pathlib import Path


class AugmentedDataset(Dataset):

    def __init__(self, root: str, transforms: dict):
        self.root = root
        self.transforms = transforms
        self.image_transform = transforms['standard']
        self.augmentation_transform = transforms['augment']

        self.img_files: list = find_files(root)

    def __len__(self):
        return len(self.img_files)

    def __getitem__(self, index):
        image: Path = self.img_files[index]

        out = {'image': self.image_transform(image), 'image_augmented': self.augmentation_transform(image)}

        return out


def find_files(root):
    files = []
    root_path: Path = Path(root)
    for file in root_path.glob('*'):
        files.append(file.absolute())
    return files


