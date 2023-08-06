from analogvnn.backward.BackwardIdentity import BackwardIdentity
from analogvnn.nn.module.Layer import Layer

__all__ = ['Normalize']


class Normalize(Layer, BackwardIdentity):
    """This class is base class for all normalization functions.
    """
    pass
