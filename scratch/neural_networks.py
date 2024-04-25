import numpy as np


class NeuralNetworks(object):
  def sigmoid(t: float) -> float:
    return 1 / (1 + np.exp(-t))