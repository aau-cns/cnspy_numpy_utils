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
import cnspy_numpy_utils.accumulated_distance as numpy_utils

class AccumulatedDistance_Test(unittest.TestCase):
    def test_accumulated_distance(self):
        arr = [0, 1, 2, 3, 4, 5, -5]
        v = np.array(arr)
        arr_acc = numpy_utils.accumulated_distance(p_vec=v)

        print('got: ' + str(arr_acc))
        self.assertTrue(arr_acc[0] == 1)

        arr_acc = numpy_utils.accumulated_distance(p_vec=np.array([]))
        print('got: ' + str(arr_acc))

        M = np.array([[0, 1, 2, 3, 4, 5], [0, 1, 2, 3, 4, 5]])
        # M = M.T
        arr_acc = numpy_utils.accumulated_distance(p_vec=M)
        print('got: ' + str(arr_acc))

    def test_total_distance(self):
        M = np.array([0, 1, 2, 3, 4, 5, -5])

        v = numpy_utils.total_distance(p_vec=M)
        print('got: ' + str(v))
        self.assertTrue(v == 15)

        v = numpy_utils.total_distance(p_vec=np.array([]))
        print('got: ' + str(v))

        M = np.array([[0, 1, 2, 3, 4, 5], [0, 1, 2, 3, 4, 5]])
        M = M.T
        v = numpy_utils.total_distance(p_vec=M)
        print('got: ' + str(v))  # sqrt(2) * 5


if __name__ == "__main__":
    unittest.main()
