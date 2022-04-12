import string
import re
import numpy as np


class RemovePunctuationTransformer(object):

	def __init__(self):
		pass


	def __call__(self, strings):
		return np.array([re.sub(r"[^A-Za-z0-9\s]", "", sample) for sample in strings])