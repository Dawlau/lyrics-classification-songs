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

		if self.transform:
			self.X = self.transform(self.X)


	def __len__(self):
		return len(self.X)


	def __getitem__(self, idx):
		X = torch.tensor(self.X[idx])
		y = torch.tensor(self.y[idx])

		return X, y