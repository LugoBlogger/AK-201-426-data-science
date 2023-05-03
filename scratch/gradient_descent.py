from scratch.linear_algebra import LinearAlgebra as la
from scratch.linear_algebra import Vector



class GradientDescent(object):
  def gradient_step(v: Vector, gradient: Vector, step_size: float) -> Vector:
    """Moves `step_size`in the `gradient` direction from `v`"""
    assert len(v) == len(gradient)
    step = la.scalar_multiply(step_size, gradient)
    return la.add(v, step)