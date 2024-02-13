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
from cnspy_numpy_utils.numpy_statistics import *

class NumpyStatistics_Test(unittest.TestCase):
    def test_vec(self):
        arr = [11, 12, 13, 22, 23, 33]
        v = np.array(arr)
        metric = numpy_statistics(v)
        print_statistics(metric)

    def test_mat(self):
        M = np.array([[11, 12, 13], [21, 22, 23], [31, 32, 33], [41, 42, 43]])

        metric = numpy_statistics(M)
        print_statistics(metric)


if __name__ == "__main__":
    unittest.main()
