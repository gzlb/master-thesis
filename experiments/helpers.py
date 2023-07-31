import scipy
from torchquad import Gaussian
from autoray import numpy as anp

class GaussLegendre(Gaussian):


    def __init__(self):
        super().__init__()
        self.name = "Gauss-Legendre"
        self._root_fn = scipy.special.roots_legendre

    @staticmethod
    def _apply_composite_rule(cur_dim_areas, dim, hs, domain):
        """Apply "composite" rule for gaussian integrals
        cur_dim_areas will contain the areas per dimension
        """
        # We collapse dimension by dimension
        for _ in range(dim):
            cur_dim_areas = anp.sum(cur_dim_areas, axis=len(cur_dim_areas.shape) - 1)
        return cur_dim_areas


