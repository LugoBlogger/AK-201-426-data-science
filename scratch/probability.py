import numpy as np

from scipy import special as sc_special




class Probability(object):
  def __init__(self):
    return None
  

  def normal_cdf(x: float, mu: float = 0, sigma: float = 1) -> float:
    return 0.5 * (1 + sc_special.erf((x - mu) / (sigma * np.sqrt(2))))


  def inverse_normal_cdf(p: float, mu: float = 0, sigma: float = 1,
    tolerance: float = 1e-5) -> float:

    """Find approximate inverse using binary search"""

    # if not standard, compute standard and rescale
    if abs(mu) > 1e-5 or abs(sigma - 1) > 1e-5:
      return mu + sigma * Probability.inverse_normal_cdf(p, tolerance=tolerance)

    low_z = -10.0         # normal_cdf(-10) is (very close to) 0
    high_z = 10.0         # normal_cdf(10) is (very close to) 1

    while high_z - low_z > tolerance:
      mid_z = (low_z + high_z) / 2      # Consider the midpoint
      mid_p = Probability.normal_cdf(mid_z)         # and the CDF's value there
      if mid_p < p:
        low_z = mid_z                   # Midpoint too low search above it
      else:
        high_z = mid_z                  # Midpoint to high, search below it

    return mid_z

  def inverse_normal_cdf_with_scipy(
    p: float, mu: float = 0, sigma: float = 1) -> float:

    return mu + sigma * np.sqrt(2) * sc_special.erfinv(2*p - 1)