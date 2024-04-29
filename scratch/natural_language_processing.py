import numpy as np

from scratch.linear_algebra import LinearAlgebra as la
from scratch.linear_algebra import Vector


class NaturalLanguageProcessing(object):
  def cosine_similarity(v1: Vector, v2: Vector) -> float:
    """Use cosine similarity to measure the similarity between two vectors"""
    return la.dot(v1, v2) / np.sqrt(la.dot(v1, v1) * la.dot(v2, v2)) 