import torch
from torch.utils.data import Dataset
from torchvision import transforms, utils


class SongsDataset(Dataset):

	def __init__(self,
		X,
		y,
		transform=transforms.Compose([])
	):

		self.X = X
		self.y = y

		self.transform = transform


	def __len__(self):
		return len(self.X)


	def __getitem__(self, idx):
		X = self.X[idx]
		y = self.y[idx]

		if self.transform:
			X = self.transform(X)

		return X, y