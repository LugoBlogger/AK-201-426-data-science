import tqdm

from typing import List
from scratch.linear_algebra import LinearAlgebra as la
from scratch.linear_algebra import Vector
from scratch.gradient_descent import GradientDescent as gd



class DimReduction(object):
  def direction(w: Vector) -> Vector:
    mag = la.magnitude(w)
    return [w_i / mag for w_i in w]

  def directional_variance(data: List[Vector], w: Vector) -> float:
    """Returns the variance of x in the direction of w"""
    w_dir = DimReduction.direction(w)
    return sum(la.dot(v, w_dir) ** 2 for v in data)

  def directional_variance_gradient(data: List[Vector], w: Vector) -> Vector:
    """The gradient of directional variance with respect to w""" 
    w_dir = DimReduction.direction(w)
    return [sum(2 * la.dot(v, w_dir) * v[i] for v in data)
              for i in range(len(w))]

  def first_principal_component(data: List[Vector], n: int = 100, 
                                step_size: float = 0.1) -> Vector:
    # Start with a random guess
    guess = [1.0 for _ in data[0]]

    with tqdm.trange(n) as t:
      for _ in t:
        dv = DimReduction.directional_variance(data, guess)
        gradient = DimReduction.directional_variance_gradient(data, guess)
        guess = gd.gradient_step(guess, gradient, step_size)
        t.set_description(f"dv: {dv:.3f}")

    return DimReduction.direction(guess)


  def project(v: Vector, w: Vector) -> Vector:
    """return the projection of v onto the direction w""" 
    projection_length = la.dot(v, w)
    return la.scalar_multiply(projection_length, w)

  def remove_projection_from_vector(v: Vector, w: Vector) -> Vector:
    """projects v onto w and subtracts the result from v""" 
    return la.subtract(v, DimReduction.project(v, w))

  def remove_projection(data: List[Vector], w: Vector) -> List[Vector]: 
    return [DimReduction.remove_projection_from_vector(v, w) for v in data]

  def pca(data: List[Vector], num_components: int) -> List[Vector]:
    components: List[Vector] = []
    for _ in range(num_components):
      component = DimReduction.first_principal_component(data)
      components.append(component)
      data = DimReduction.remove_projection(data, component)

    return components

  def transform_vector(v: Vector, components: List[Vector]) -> Vector:
    return [la.dot(v, w) for w in components]

  def transform(data: List[Vector], components: List[Vector]) -> List[Vector]:
    return [DimReduction.transform_vector(v, components) for v in data]

