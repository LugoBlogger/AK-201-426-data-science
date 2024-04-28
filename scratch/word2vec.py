import numpy as np
import json

from typing import Iterable, List, Tuple
from scratch.linear_algebra import LinearAlgebra as la
from scratch.linear_algebra import Vector
from scratch.deep_learning import DeepLearning as dl
from scratch.deep_learning import Tensor, Layer



class Vocabulary(object):
  def __init__(self, words: List[str] = None) -> None:
    self.w2i: Dict[str, int] = {}   # mapping word -> word_id
    self.i2w: Dict[int, str] = {}   # mapping word_id -> word

    for word in (words or []):      # If words were provided
      self.add(word)                # add them.

  @property 
  def size(self) -> int:
    """how many words are in the vocabulary""" 
    return len(self.w2i)

  def add(self, word: str) -> None:
    if word not in self.w2i:        # If the word is new to us:
      word_id = len(self.w2i)       # Find the next id. 
      self.w2i[word] = word_id      # Add to the word -> word_id map. 
      self.i2w[word_id] = word      # Add to the word_id -> word map. 

  def get_id(self, word: str) -> int: 
    """return the id of the word (or None)""" 
    return self.w2i.get(word)

  def get_word(self, word_id: int) -> str:
    """return the word with the given id (or None)""" 
    return self.i2w.get(word_id)

  def one_hot_encode(self, word: str) -> Tensor:
    word_id = self.get_id(word)
    assert word_id is not None, f"unknown word {word}"

    return [1.0 if i == word_id else 0.0 for i in range(self.size)]


class Word2Vec(object):
  def cosine_similarity(v1: Vector, v2: Vector) -> float:
    """Use cosine similarity to measure the similarity between two vectors"""
    return la.dot(v1, v2) / np.sqrt(la.dot(v1, v1) * la.dot(v2, v2)) 

  def save_vocab(vocab: Vocabulary, filename: str) -> None:
    with open(filename, 'w') as f:
      json.dump(vocab.w2, f)        # only need to save w2i

  def load_vocab(filename: str) -> Vocabulary:
    vocab = Vocabulary()
    with open(filename) as f:
      # Load w2i and generate i2w from it
      vocab.w2i = json.load(f)
      vocab.i2w = {id: word for word, id in vocab.w2i.items()}

    return vocab


class Embedding(Layer):
  def __init__(self, num_embeddings: int, embedding_dim: int, rng) -> None:
    self.num_embeddings = num_embeddings
    self.embedding_dim = embedding_dim

    # One vector of size embedding_dim for each desired embedding
    self.embeddings = dl.random_tensor(num_embeddings, embedding_dim, rng=rng)
    self.grad = dl.zeros_like(self.embeddings)

    # Save last input id
    self.last_input_id = None

  # Define `forward` pass to do embedding one word at a time
  def forward(self, input_id: int) -> Tensor:
    """Just select the embedding vector corresponding to the input id""" 
    self.input_id = input_id    # remember for use in backpropagation
    return self.embeddings[input_id]

  # Define the corresponding `backward` pass and the corresponding gradient
  def backward(self, gradient: Tensor) -> None:
    # Zero out the gradient corresponding to the last input.
    # This is way cheaper than creating a new all-zero tensor each time.
    if self.last_input_id is not None:
      zero_row = [0 for _ in range(self.embedding_dim)]
      self.grad[self.last_input_id] = zero_row


    self.last_input_id = self.input_id
    self.grad[self.input_id] = gradient

  # We need to override the default function of params and gradients
  def params(self) -> Iterable[Tensor]:
    return [self.embeddings]

  def grads(self) -> Iterable[Tensor]:
    return [self.grad]


class TextEmbedding(Embedding):
  def __init__(self, vocab: Vocabulary, embedding_dim: int, rng) -> None:
    # Call the superclass constructor
    super().__init__(vocab.size, embedding_dim, rng)

    # And hang onto the vocab
    self.vocab = vocab

  # We'd like to be able to retrieve the vector for a given word
  def __getitem__(self, word: str) -> Tensor:
    word_id = self.vocab.get_id(word)
    if word_id is not None:
      return self.embeddings[word_id]
    else: 
      return None 

  # We'd also like the embedding layer to tell us the closest words to 
  # a given word
  def closest(self, word: str, n: int = 5) -> List[Tuple[float, str]]:
    """Returns the n closest words based on cosine similarity""" 
    vector = self[word]

    # Compute pairs (similarity, other_word), and sort most similar first
    scores = [(Word2Vec.cosine_similarity(vector, self.embeddings[i]), other_word) 
                for other_word, i in self.vocab.w2i.items()]

    scores.sort(reverse=True)

    return scores[:n]