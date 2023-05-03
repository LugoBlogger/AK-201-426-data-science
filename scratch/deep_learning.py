from typing import List, Callable, Iterable
from scratch.probability import Probability as prob

Tensor = list


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

  def tensor_apply(f: Callable[[float], float], tensor: Tensor) -> Tensor:
    """Applies f elemenwise""" 
    if DeepLearning.is_1d(tensor):
      return [f(x) for x in tensor]
    else:
      return [DeepLearning.tensor_apply(f, tensor_i) for tensor_i in tensor]

  def zeros_like(tensor: Tensor) -> Tensor:
    return DeepLearning.tensor_apply(lambda _: 0.0, tensor)


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

  def random_tensor(*dims: int, init: str = "normal", 
                    rng=np.random.default_rng()) -> Tensor:
    if init == "normal":
      return DeepLearning.random_normal(*dims, rng=rng)
    elif init == "uniform":
      return DeepLearning.random_uniform(*dims, rng=rng)
    elif init == "xavier":
      variance = len(dims) / sum(dims)
      return DeepLearning.random_normal(*dims, variance=variance, rng=rng)


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