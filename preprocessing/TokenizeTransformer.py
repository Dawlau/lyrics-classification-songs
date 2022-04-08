


class TokenizeTransformer(object):

	def __init__(self, tokenizer):
		"""
			Init the transformer
			Parameters:
				tokenizer: Callable for tokenizing a string
		"""
		self.tokenizer = tokenizer


	def __call__(self, string):
		return self.tokenizer(string)