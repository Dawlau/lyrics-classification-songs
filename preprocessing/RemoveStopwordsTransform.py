import nltk
from nltk.corpus import stopwords


class RemoveStopwordsTransform(object):

	def __init__(self, language="english"):
		self.stop_words = stopwords.words(language)


	def __call__(self, tokens):
		return [token for token in tokens if token not in self.stop_words]