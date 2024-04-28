import numpy as np

from typing import List, Callable, Iterable
from scratch.probability import Probability as prob
from scratch.linear_algebra import LinearAlgebra as la

Tensor = list

class Layer(object):
  """Our neural networks will be composed of Layers, each of which
     knows how to do some computation on its inputs in the `forward`
     direction and propagate gradients in the `backward` direction."""

  def forward(self, input):
    """Note the lack of types. We're not going to be prescriptive
       about what kinds of inputs layers can take and what kinds
       of outputs they can return.""" 
    
    raise NotImplementedError 


  def backward(self, gradient):
    """Similarly, we're not going to be prescriptive about what the
       gradient looks like. It's up to you the user to make sure
       that you're doing things sensibly.""" 
    
    raise NotImplementedError


  def params(self) -> Iterable[Tensor]:
    """Returns the parameters of this layer. The default implementation
       returns nothing, so that if you have a layer with no parameters
       you don't have to implement this.""" 

    return ()


  def grads(self) -> Iterable[Tensor]:
    """Returns the gradients, in the same order as params().""" 
    return ()

class DeepLearning(object):
  def shape(tensor: Tensor) -> List[int]:
    sizes: List[int] = []
    while isinstance(tensor, list):
      sizes.append(len(tensor))
      tensor = tensor[0]
    return sizes

  def is_1d(tensor: Tensor) -> bool:
    """If tensor[0] is a list, it's a higher-order tensor.
       Otherwise, tensor is 1-dimensional (that is, a vector)."""
    return not isinstance(tensor[0], list)

  def tensor_sum(tensor: Tensor) -> float:
    """Sums up all the values in the tensor""" 
    if DeepLearning.is_1d(tensor):
      return sum(tensor)        # just a list of floats, use Python sum
    else:
      return sum(DeepLearning.tensor_sum(tensor_i   # Call tensor_sum on each row
                  for tensor_i in tensor))          # and sum up those results.

  def tensor_apply(f: Callable[[float], float], tensor: Tensor) -> Tensor:
    """Applies f elemenwise""" 
    if DeepLearning.is_1d(tensor):
      return [f(x) for x in tensor]
    else:
      return [DeepLearning.tensor_apply(f, tensor_i) for tensor_i in tensor]

  def zeros_like(tensor: Tensor) -> Tensor:
    return DeepLearning.tensor_apply(lambda _: 0.0, tensor)

  def tensor_combine(f: Callable[[float, float], float],
                      t1: Tensor, t2: Tensor) -> Tensor:
    """Applies f to corresponding elements of t1 and t2""" 
    if DeepLearning.is_1d(t1):
      return [f(x, y) for x, y in zip(t1, t2)]
    else: 
      return [DeepLearning.tensor_combine(f, t1_i, t2_i)
              for t1_i, t2_i in zip(t1, t2)]


  def random_uniform(*dims: int, rng=None) -> Tensor:
    if len(dims) == 1:
      return [rng.random() for _ in range(dims[0])]
    else:
      return [DeepLearning.random_uniform(*dims[1:], rng=rng) 
              for _ in range(dims[0])]

  def random_normal(*dims: int, mean: float = 0.0, 
                    variance: float = 1.0, rng = None) -> Tensor:
    if len(dims) == 1:
      return [mean + variance * prob.inverse_normal_cdf(rng.random())
              for _ in range(dims[0])]
    else:
      return [DeepLearning.random_normal(*dims[1:], mean=mean, 
                                          variance=variance, rng=rng)
              for _ in range(dims[0])]

  def random_tensor(*dims: int, init: str = "normal", rng=None) -> Tensor:
    if init == "normal":
      return DeepLearning.random_normal(*dims, rng=rng)
    elif init == "uniform":
      return DeepLearning.random_uniform(*dims, rng=rng)
    elif init == "xavier":
      variance = len(dims) / sum(dims)
      return DeepLearning.random_normal(*dims, variance=variance, rng=rng)
    else:
      raise ValueError(f"unknown init: {init}")  

  def one_hot_encode(i: int, num_labels: int = 10) -> List[float]:
    return [1.0 if j == i else 0.0 for j in range(num_labels)]


  def softmax(tensor: Tensor) -> Tensor:
    """Softmax along the last dimension"""
    if DeepLearning.is_1d(tensor):
      # Subtract largest value for numerical stability
      largest = max(tensor)
      exps = [np.exp(x - largest) for x in tensor]

      sum_of_exps = sum(exps)
      return [exp_i / sum_of_exps for exp_i in exps]

    else:
      return [DeepLearning.softmax(tensor_i) for tensor_i in tensor]

  def tanh(x: float) -> float:
    # If x is very large or very small, tanh is (essentially) 1 or -1.
    # We check for this becasue, e.g., np.exp(1_000) raises an error.
    if x < -100:
      return -1
    if x > 100:
      return 1

    em2x = np.exp(-2 * x)
    return (1 - em2x) / ( 1 + em2x)


  def save_weights(model: Layer, filename: str) -> None:
    weights = list(model.params())
    with open(filename, 'w') as f:
      json.dump(weights, f)


  def load_weights(model: Layer, filename: str) -> None:
    with open(filename) as f:
      weights = json.load(f)

    # Check for consistency
    assert all(shape(param) == shape(weight)
                for param, weight in zip(model.params(), weights))

    # Then load using slice assignment
    for param, weight in zip(model.params(), weights):
      param[:] = weight


class Linear(Layer):
  def __init__(self, input_dim: int, output_dim: int, init: 
                str = "xavier", rng=None) -> None:
    """A layer of output_dim neurons, each with input_dim weights
       (and a bias).""" 

    self.input_dim = input_dim 
    self.output_dim = output_dim 

    # self.w[o] is the weights for the o-th neuron
    self.w = DeepLearning.random_tensor(output_dim, input_dim, 
                                        init=init, rng=rng)
    
    # self.b[o] is the bias term for the o-th neuron
    self.b = DeepLearning.random_tensor(output_dim, init=init, rng=rng)
  

  def forward(self, input: Tensor) -> Tensor: 
    # Save the input to use in the backward pass.
    self.input = input

    # Return the vector of neuron outputs.
    return [la.dot(input, self.w[o]) + self.b[o]
            for o in range(self.output_dim)]


  def backward(self, gradient: Tensor) -> Tensor:
    # Each b[o] gets added to output[o], which means 
    # the gradient of b is the same as the output gradient
    self.b_grad = gradient
    
    # Each w[o][i] multiplies input[i] and gets added to output[o]. 
    # So its gradient is input[i] * gradient[o]. 
    self.w_grad = [[self.input[i] * gradient[o]
                    for i in range(self.input_dim)]
                   for o in range(self.output_dim)] 

    # Each input[i] multiplies every w[o][i] and gets added to every output[o]. 
    # So its gradient is the sum of w[o][i] * gradient[o]
    # across all the outputs.
    return [sum(self.w[o][i] * gradient[o] for o in range(self.output_dim))
            for i in range(self.input_dim)]

    
  def params(self) -> Iterable[Tensor]:
    return [self.w, self.b]

  
  def grads(self) -> Iterable[Tensor]:
    return [self.w_grad, self.b_grad]


class Sequential(Layer):
  """A layer consisting of a sequence of other layers. It's up to you to make
     sure that the output of each layer makes sense as the input to the
     next layer.""" 

  def __init__(self, layers: List[Layer]) -> None: 
    self.layers = layers

  def forward(self, input):
    """Just forward the input through the layers in order.""" 
    for layer in self.layers:
      input = layer.forward(input)

    return input  

  def backward(self, gradient):
    """Just backpropagate the gradient through the layers in reverse.""" 
    for layer in reversed(self.layers):
      gradient = layer.backward(gradient)

    return gradient


  def params(self) -> Iterable[Tensor]:
    """Just return the params from each layer.""" 
    return (param for layer in self.layers for param in layer.params())

  def grads(self) -> Iterable[Tensor]:
    """Just return the grads from each layer.""" 
    return (grad for layer in self.layers
              for grad in layer.grads())


class Loss(object):
  def loss(self, predicted: Tensor, actual: Tensor) -> float:
    """How good are our predictions? (Larger numbers are worse.)""" 
    raise NotImplementedError

  def gradient(self, predicted: Tensor, actual: Tensor) -> Tensor: 
    """How does the loss change as the predictions change?""" 
    raise NotImplementedError
    


class Optimizer(object):
  """An optimizer updates the weights of a layer (in place) using information
     known by either the layer or the optimzer (or by both).""" 
  def step(self, layer: Layer) -> None: 
    raise NotImplementedError


class GradientDescent(Optimizer):
  def __init__(self, learning_rate: float = 0.1) -> None:
    self.lr = learning_rate

  def step(self, layer: Layer) -> None:
    for param, grad in zip(layer.params(), layer.grads()):
      # Update param using a gradient step
      param[:] = DeepLearning.tensor_combine(
        lambda param, grad: param - grad * self.lr, 
        param, grad)


class Momentum(Optimizer):
  def __init__(self, learning_rate: float, momentum: float = 0.9) -> None: 
    self.lr = learning_rate 
    self.mo = momentum 
    self.updates: List[Tensor] = []   # running average
    
  def step(self, layer: Layer) -> None: 
    # If we have no previous updates, start with all zeros 
    if not self.updates:
      self.updates = [DeepLearning.zeros_like(grad) for grad in layer.grads()]

    for update, param, grad in zip(self.updates, layer.params(), 
                                    layer.grads()):
      # Apply momentum
      update[:] = DeepLearning.tensor_combine(
        lambda u, g: self.mo * u + (1 - self.mo) * g, 
        update, grad)

      # Then take a gradient step
      param[:] = DeepLearning.tensor_combine(
        lambda p, u: p - self.lr * u, 
        param, update)


class SoftmaxCrossEntropy(Loss):
  """This is the negative-log-likelihood of the observed values, given the
     neural net model. So if we choose weights to minimize it, our model will
     be maximizing the likelihood of the observed data.""" 

  def loss(self, predicted: Tensor, actual: Tensor) -> float: 
    # Apply softmax to get probabilities
    probabilities = DeepLearning.softmax(predicted)

    # This will be log p_i for the actual class i and 0 for the other
    # classes. We add a tiny amount to p to avoid taking log(0). 
    likelihoods = DeepLearning.tensor_combine(
      lambda p, act: np.log(p + 1e-30) * act, 
      probabilities, actual)

    # And then we just sum up the negatives.
    return -DeepLearning.tensor_sum(likelihoods)

  def gradient(self, predicted: Tensor, actual: Tensor) -> Tensor:
    probabilities = DeepLearning.softmax(predicted)

    # Isn't this a pleasant equation?
    return DeepLearning.tensor_combine(
      lambda p, actual: p - actual, 
      probabilities, actual)