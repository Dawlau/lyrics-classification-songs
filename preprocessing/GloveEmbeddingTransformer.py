from collections import Counter
import numpy as np


class GloveEmbeddingTransformer(object):

	def __init__(self, words, k, max_length, embeddings_file="glove.6B.100d.txt"):

		self.max_length = max_length
		with open(embeddings_file, "r") as r:
			lines = r.readlines()
			lines = [line.split() for line in lines]
			self.vocab = {line[0] for line in lines}
			self.words = {word for word in words if word in self.vocab}
			most_common = Counter(self.vocab & self.words).most_common(k)
			self.word_to_idx = {x: i + 2 for i, (x, freq) in enumerate(most_common)}
			self.word_to_idx["<unk>"] = 1
			self.word_to_idx["<pad>"] = 0
			self.embeddings	= [(self.word_to_idx[line[0]], line[1 : ]) for line in lines if line[0] in self.word_to_idx]
			self.embeddings.sort(key=lambda x : x[0])
			self.embeddings = np.array([x for _, x in self.embeddings], dtype=np.float32)

		embedding_length = len(self.embeddings[0])
		unk_embedding = np.mean(self.embeddings, axis=0, keepdims=True)
		pad_embedding = np.zeros((1, embedding_length))
		self.embeddings = np.vstack((pad_embedding, unk_embedding, self.embeddings))

	def get_embeddings(self):
		return self.embeddings


	def __call__(self, sentences):
		result = [[self.word_to_idx[token] if token in self.word_to_idx else 0 for token in sentence] for sentence in sentences]
		result = [sentence[ : self.max_length] for sentence in result]
		result = [sentence + [1] * max(0, self.max_length - len(sentence)) for sentence in result]
		return np.array(result)