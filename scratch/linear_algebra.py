import numpy as np
from typing import List, Callable, Tuple

Vector = List[float]
Matrix = List[List[float]]


class LinearAlgebra(object):
  def __init__(self):
    return None

  def add(v: Vector, w: Vector) -> Vector:
    """Adds corresponding elements"""
    assert len(v) == len(w), "vectors must be the same length"
    return [v_i + w_i for v_i, w_i in zip(v, w)]

  def subtract(v: Vector, w: Vector) -> Vector:
    """Subtracts corresponding elements"""
    assert len(v) == len(w), "vectors must be the same length"
    return [v_i - w_i for v_i, w_i in zip(v, w)]

  def vector_sum(vectors: List[Vector]) -> Vector:
    """Sum all corresponding elements"""
    # Check that vectors is not empty
    assert vectors, "no vectors provided!"

    # Check the vectors are all the same size
    num_elements = len(vectors[0])
    assert all(len(v) == num_elements for v in vectors), "different sizes!"

    # the i-th element of the result is the sum of every vector[i]
    return [sum(vector[i] for vector in vectors)
            for i in range(num_elements)]

  def scalar_multiply(c: float, v: Vector) -> Vector:
    """Multiplies every element by c""" 
    return [c * v_i for v_i in v]

  def vector_mean(vectors: List[Vector]) -> Vector:
    """Computes the element-wise average""" 
    n = len(vectors)
    return LinearAlgebra.scalar_multiply(1/n, LinearAlgebra.vector_sum(vectors))

  def dot(v: Vector, w: Vector) -> float:
    """Computes v_1 * w_1 + ... + v_n * w_n"""
    assert len(v) == len(w), "vectors must be the same length"

    return sum(v_i * w_i for v_i, w_i in zip(v, w))

  def sum_of_squares(v: Vector) -> float:
    """Returns v_1 * v_1 + ... + v_n * v_n"""
    return LinearAlgebra.dot(v, v)

  def magnitude(v: Vector) -> float:
    """Returns the magnitude (or length) of v"""
    return np.sqrt(LinearAlgebra.sum_of_squares(v))

  def squared_distance(v: Vector, w: Vector) -> float:
    """Computes (v_1 - w_1)**2 + ... + (v_n - w_n)**2"""
    return LinearAlgebra.sum_of_squares(LinearAlgebra.subtract(v, w))

  def distance(v: Vector, w: Vector) -> float:    
    """Computes the distance between v and w"""
    return np.sqrt(LinearAlgebra.squared_distance(v, w))

  def shape(A: Matrix) -> Tuple[int, int]:
    """Returns (# of rows of A, # of columns of A)"""
    num_rows = len(A)
    num_cols = len(A[0]) if A else 0      # number of elements in first row
    return num_rows, num_cols

  def make_matrix(num_rows: int, num_cols: int,
    entry_fn: Callable[[int, int], float]) -> Matrix:

    """ 
    Return a num_rows x num_cols matrix whose (i,j)-th entry
    is entry_fn(i,j)
    """
    return [[entry_fn(i,j)                  # given i, create a list
              for j in range(num_cols)]     # [entry_fn(i, 0), ...]
                for i in range(num_rows)]   # create one list for each i  

