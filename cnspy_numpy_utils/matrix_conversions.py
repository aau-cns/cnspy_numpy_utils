#!/usr/bin/env python
# Software License Agreement (GNU GPLv3  License)
#
# Copyright (c) 2020, Roland Jung (roland.jung@aau.at) , AAU, KPK, NAV
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
#
# Requirements:
# numpy
########################################################################################################################
import numpy as np


def tri_vec_to_mat(tri_vec, n=None):
    """"
    converts an upper triangular vector into a symmetric matrix.
    Example:
    >>    v = np.array([11, 12, 13, 22, 23, 33])
    >>    M = tri_vec_to_mat(tri_vec=v, n=3)  # [[11, 12, 13], [21, 22, 23], [31, 32, 33]]

    Input:
    tri_vec -- numpy.ndarray, vector [1xM],

    Output:
    P -- numpy.ndarray, square matrix [NxN]
    """

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
    """"
    converts an upper triangular matrix of a symmetric matrix into a vector.

    Example:
    >> import numpy as np
    >> from cnspy_numpy_utils.matrix_conversions import *
    >> M = np.array([[11, 12, 13], [21, 22, 23], [31, 32, 33]])
    >> v = mat_to_tri_vec(P=M) # [11 12 13 22 23 33]
    >> M2 = np.array([[11, 12, 13, 14, 15 ,16], [21, 22, 23, 24, 25, 26], [31, 32, 33, 34, 35, 36], [41,42,43,44,45,46], [51,52,53,54,55,56], [61,62,63,64,65,66]])
    >> v2 = mat_to_tri_vec(P=M2) # [11 12 13 14 15 16 22 23 24 25 26 33 34 35 36 44 45 46 55 56 66]
    >> print(v2)

    Input:
    P -- numpy.ndarray, square matrix [NxN]

    Output:
    tri_vec -- numpy.ndarray, vector [1xM],
    """
    n = P.shape[0]
    # m = n * (n + 1) / 2
    idxs = np.triu_indices(n=n, k=0)
    return P[idxs]

