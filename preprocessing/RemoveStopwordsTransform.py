import nltk
from nltk.corpus import stopwords
import numpy as np


class RemoveStopwordsTransform(object):

	def __init__(self, language="english"):
		self.stop_words = stopwords.words(language)


	def __call__(self, tokens):
		return np.array([token for token in tokens if token not in self.stop_words])