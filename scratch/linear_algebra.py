import numpy as np
from typing import List, Callable

Vector = List[float]
Matrix = List[List[float]]


class LinearAlgebra(object):
  def __init__(self):
    return None

  def subtract(v: Vector, w: Vector) -> Vector:
    """Subtracts corresponding elements"""
    assert len(v) == len(w), "vectors must be the same length"
    return [v_i - w_i for v_i, w_i in zip(v, w)]

  def dot(v: Vector, w: Vector) -> float:
    """Computes v_1 * w_1 + ... + v_n * w_n"""
    assert len(v) == len(w), "vectors must be the same length"

    return sum(v_i * w_i for v_i, w_i in zip(v, w))

  def sum_of_squares(v: Vector) -> float:
    """Returns v_1 * v_1 + ... + v_n * v_n"""
    return LinearAlgebra.dot(v, v)

  def make_matrix(num_rows: int, num_cols: int,
    entry_fn: Callable[[int, int], float]) -> Matrix:

    """ 
    Return a num_rows x num_cols matrix whose (i,j)-th entry
    is entry_fn(i,j)
    """
    return [[entry_fn(i,j)                  # given i, create a list
              for j in range(num_cols)]     # [entry_fn(i, 0), ...]
                for i in range(num_rows)]   # create one list for each i  

  def squared_distance(v: Vector, w: Vector) -> float:
    """Computes (v_1 - w_1)**2 + ... + (v_n - w_n)**2"""
    return LinearAlgebra.sum_of_squares(subtract(v, w))

  def distance(v: Vector, w: Vector) -> float:    
    """Computes the distance between v and w"""
    return np.sqrt(LinearAlgebra.squared_distance(v, w))

