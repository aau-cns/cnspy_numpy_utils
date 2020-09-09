#!/usr/bin/env python
# Software License Agreement (GNU GPLv3  License)
#
# Copyright (c) 2018, Roland Jung (roland.jung@aau.at) , AAU, KPK, NAV
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


def numpy_statistics(vNumpy):
    metrics = {
        'pairs': len(vNumpy),
        'rmse': np.sqrt(np.dot(vNumpy, vNumpy) / len(vNumpy)),
        'mean': np.mean(vNumpy),
        'median': np.median(vNumpy),
        'std': np.std(vNumpy),
        'var': np.square(np.std(vNumpy)),
        'min': np.min(vNumpy),
        'max': np.max(vNumpy)
    }
    return metrics


def print_statistics(metrics, desc='error'):
    print ("samples   %d" % (metrics['pairs']))
    print ("%s.rmse   %f m" % (str(desc), metrics['rmse']))
    print ("%s.mean   %f m" % (str(desc), metrics['mean']))
    print ("%s.median %f m" % (str(desc), metrics['median']))
    print ("%s.std    %f m" % (str(desc), metrics['std']))
    print ("%s.var    %f m" % (str(desc), metrics['var']))
    print ("%s.min    %f m" % (str(desc), metrics['min']))
    print ("%s.max    %f m" % (str(desc), metrics['max']))
