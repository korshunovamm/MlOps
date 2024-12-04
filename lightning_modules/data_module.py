import os
import torch
from torch.utils.data import Dataset, DataLoader
from torchvision import transforms
from torchvision.datasets import CIFAR10
from pytorch_lightning import LightningDataModule, LightningModule
from chebyshevDistance import ChebyshevDistance
import torch.nn as nn
import torch.nn.functional as F
import numpy as np


# Кастомный Dataset с вычислением Чебышёвского расстояния
class CIFAR10Dataset(Dataset):
    def __init__(self, data_dir, train=True, transform=None, download=False):
        self.data = CIFAR10(root=data_dir, train=train, download=download)
        self.transform = transform

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        # Получаем изображение и метку
        image, label = self.data[idx]

        if self.transform:
            image = self.transform(image)

        # Чебышёвское расстояние между двумя случайными векторами
        vector_size = 10
        v1 = np.random.rand(vector_size).tolist()
        v2 = np.random.rand(vector_size).tolist()
        distance = ChebyshevDistance.chebyshevDistance(v1, v2)

        return image, label

class CIFAR10DataModule(LightningDataModule):
    def __init__(self, data_dir, batch_size):
        super().__init__()
        self.data_dir = data_dir
        self.batch_size = batch_size
        self.transform = transforms.Compose([
            transforms.ToTensor(),
            transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))
        ])
        self.train_dataset = None
        self.val_dataset = None

    def setup(self, stage=None):
            # if stage == 'fit' or stage is None:
        self.train_dataset = CIFAR10(root=self.data_dir, train=True, download=True, transform=self.transform)
        self.val_dataset = CIFAR10(root=self.data_dir, train=False, download=True, transform=self.transform)

    # def setup(self, stage=None):
    #     self.train_dataset = MNISTDataset(self.data_dir, train=True, transform=self.transform, download=True)
    #     self.val_dataset = MNISTDataset(self.data_dir, train=False, transform=self.transform, download=True)

    def train_dataloader(self):
        return DataLoader(self.train_dataset, batch_size=self.batch_size, shuffle=True)

    def val_dataloader(self):
        return DataLoader(self.val_dataset, batch_size=self.batch_size)

class CIFAR10Classifier(LightningModule):
    def __init__(self, lr):
        super().__init__()
        self.save_hyperparameters()
        self.model = nn.Sequential(
            nn.Conv2d(3, 32, kernel_size=3, stride=1, padding=1),
            nn.ReLU(),
            nn.MaxPool2d(kernel_size=2, stride=2),
            nn.Conv2d(32, 64, kernel_size=3, stride=1, padding=1),
            nn.ReLU(),
            nn.MaxPool2d(kernel_size=2, stride=2),
            nn.Flatten(),
            nn.Linear(64 * 8 * 8, 128),  # Размер выхода 64 фильтра * 8 * 8 после свёртки
            nn.ReLU(),
            nn.Linear(128, 10)  # 10 классов для CIFAR-10
        )
        self.criterion = nn.CrossEntropyLoss()
        self.lr = lr

    def forward(self, x):
        return self.model(x)

    def training_step(self, batch, batch_idx):
        X, y = batch
        preds = self(X)
        loss = self.criterion(preds, y)
        self.log("train_loss", loss, on_step=True, on_epoch=True, prog_bar=True, logger=True)
        return loss

    def validation_step(self, batch, batch_idx):
        X, y = batch
        preds = self(X)
        loss = self.criterion(preds, y)
        acc = (preds.argmax(dim=1) == y).float().mean()
        self.log("val_loss", loss, on_epoch=True, prog_bar=True, logger=True)
        self.log("val_acc", acc, on_epoch=True, prog_bar=True, logger=True)
        return loss

    def configure_optimizers(self):
        return torch.optim.Adam(self.parameters(), lr=self.lr)





# class MNISTDataset(Dataset):
#     def __init__(self, data_dir, train=True, transform=None, download=False):
#         self.data = MNIST(root=data_dir, train=train, download=True)
#         self.transform = transform

#     def __len__(self):
#         return len(self.data)

#     def __getitem__(self, idx):
#         # Загружаем изображение и метку
#         image, label = self.data[idx]
#         if self.transform:
#             image = self.transform(image)

#         # Вычисляем след
#         vector_size = 10
#         v1 = np.random.rand(vector_size).tolist()
#         v2 = np.random.rand(vector_size).tolist()
#         distance = ChebyshevDistance.chebyshevDistance(v1, v2)

#         return image, label
