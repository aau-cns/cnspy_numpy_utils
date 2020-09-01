import numpy as np
import math


def tri_vec_to_mat(tri_vec, n=None):
    if n is None:
        m = len(tri_vec)
        # m = n(n+1)/2
        # solve: n^2 + n - 2m = 0
        coeff = [1, 1, -2 * m]
        [s1, s2] = np.roots(coeff)
        n = max(s1, s2)

    n = int(n)
    idxs = np.triu_indices(n=n, k=0)
    P = np.zeros((n, n))
    P[idxs] = tri_vec
    P = P + P.T - np.diag(np.diag(P))
    return P


def mat_to_tri_vec(P):
    n = P.shape[0]
    # m = n * (n + 1) / 2
    idxs = np.triu_indices(n=n, k=0)
    return P[idxs]
