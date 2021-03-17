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
import unittest
import numpy as np
import cnspy_numpy_utils.matrix_conversions as matrix_conversions

class MatrixConversion_Test(unittest.TestCase):
    def test_tri_vec_to_mat(self):
        arr = [11, 12, 13, 22, 23, 33]
        v = np.array(arr)
        M = matrix_conversions.tri_vec_to_mat(tri_vec=v, n=3)

        print('got: ' + str(M))
        self.assertTrue(M[3 - 1, 2 - 1] == 23)
        self.assertTrue(M[1 - 1, 2 - 1] == 12)

    def test_mat_to_tri_vec(self):
        M = np.array([[11, 12, 13], [21, 22, 23], [31, 32, 33]])

        v = matrix_conversions.mat_to_tri_vec(P=M)
        print('got: ' + str(v))
        self.assertTrue(v[3] == 22)


if __name__ == "__main__":
    unittest.main()
