


class TokenizeTransformer(object):

	def __init__(self, tokenizer):
		"""
			Init the transformer
			Parameters:
				tokenizer: Callable for tokenizing a string
		"""
		self.tokenizer = tokenizer


	def __call__(self, sample):
		return self.tokenizer(string)