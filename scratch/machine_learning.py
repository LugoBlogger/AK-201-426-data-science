import numpy as np

from typing import TypeVar, List, Tuple


X = TypeVar('X')


class MachineLearning(object):
  def __init__(self):
    return None


  def split_data(data: List[X], prob: float, rng) \
      -> Tuple[List[X], List[X]]:

    """Split data into fraction [prob, 1 - prob]""" 
    data = data[:]

    rng.shuffle(data)             # because shuffle modifies the list
    cut = int(len(data) * prob)   # Use prob to find a cutoff
    return data[:cut], data[cut:]