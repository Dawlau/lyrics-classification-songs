import numpy as np


class TokenizeTransformer(object):

	def __init__(self, tokenizer):
		"""
			Init the transformer
			Parameters:
				tokenizer: Callable for tokenizing a string
		"""
		self.tokenizer = tokenizer


	def __call__(self, strings):
		return [self.tokenizer(sample) for sample in strings]