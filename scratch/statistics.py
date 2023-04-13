import numpy as np


from typing import List
from scratch.linear_algebra import LinearAlgebra as la



class Statistics(object):
  def __init__(self):
    return None

  def mean(xs: List[float]) -> float:
    return sum(xs) / len(xs)
  
  def de_mean(xs: List[float]) -> List[float]:
    """Translate xs by subtracting its mean (so the result has mean 0)"""
    x_bar = Statistics.mean(xs)
    return [x - x_bar for x in xs]

  def variance(xs: List[float]) -> float:
    """Almost the average squared deviation from the mean"""
    assert len(xs) >= 2, "variance requries at least two elements"

    n = len(xs)
    deviations = Statistics.de_mean(xs)
    return la.sum_of_squares(deviations) / (n - 1)

  def standard_deviation(xs: List[float]) -> float:
    """The standard deviation is the square root of the variance"""
    return np.sqrt(Statistics.variance(xs))

  def covariance(xs: List[float], ys: List[float]) -> float:
    """Arguments:
        - xs [List] = list of float number"""
    assert len(xs) == len(ys), "xs and ys must have the same number of elements"

    return la.dot(Statistics.de_mean(xs), Statistics.de_mean(ys)) / (len(xs) - 1)

  def correlation(xs: List[float], ys: List[float]) -> float:
    """Measures how much xs and ys vary in tandem about their means"""
    stdev_x = Statistics.standard_deviation(xs)
    stdev_y = Statistics.standard_deviation(ys)

    if stdev_x > 0  and stdev_y > 0:
      return Statistics.covariance(xs, ys) / stdev_x / stdev_y
    else:
      return 0        # if no variation, correlation is zero
