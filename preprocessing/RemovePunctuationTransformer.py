import string
import re


class RemovePunctuationTransformer(object):

	def __init__(self):
		pass


	def __call__(self, sample):
		return re.sub(r"[^A-Za-z0-9\s]", "", sample)