import torch
from torch.utils.data import Dataset
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder


THRESHOLD_YEAR = 2006
LABELS = ['Pop', 'Hip-Hop', 'Rock', 'Metal']
SEED = 42


def get_label_encoder(path_to_dataset):
	dataset = pd.read_csv(path_to_dataset)
	dataset = dataset[dataset["year"] >= THRESHOLD_YEAR]
	dataset = dataset[dataset["genre"].isin(LABELS)]

	X = dataset["lyrics"].to_numpy()
	y = dataset["genre"].to_numpy()

	return  LabelEncoder().fit(y)


def get_dataset_splits(path_to_dataset, train_size_p, val_size_p=0.0):
	dataset = pd.read_csv(path_to_dataset)
	dataset = dataset[dataset["year"] >= THRESHOLD_YEAR]
	dataset = dataset[dataset["genre"].isin(LABELS)]

	X = dataset["lyrics"].to_numpy()
	y = dataset["genre"].to_numpy()
	y = LabelEncoder().fit(y).transform(y)

	X_train, X, y_train, y = train_test_split(
		X,
		y,
		train_size=train_size_p,
		random_state=SEED,
		stratify=y
	)

	if val_size_p == 0:
		X_test, y_test = X, y
		return X_train, y_train, X_test, y_test

	X_val, X_test, y_val, y_test = train_test_split(
		X,
		y,
		train_size=val_size_p / (1 - train_size_p),
		random_state=SEED,
		stratify=y
	)

	return X_train, y_train, X_val, y_val, X_test, y_test