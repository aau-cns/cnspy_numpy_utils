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


def numpy_statistics(vNumpy, prefix=''):
    if prefix:
        metrics = {
            prefix + '.pairs': len(vNumpy),
            prefix + '.rmse': np.sqrt(np.square(vNumpy).mean(axis=0)),
            prefix + '.mean': np.mean(vNumpy, axis=1),
            prefix + '.median': np.median(vNumpy),
            prefix + '.std': np.std(vNumpy),
            prefix + '.var': np.square(np.std(vNumpy)),
            prefix + '.min': np.min(vNumpy),
            prefix + '.max': np.max(vNumpy)
        }
    else:
        metrics = {
            'pairs': len(vNumpy),
            'rmse': np.sqrt(np.square(vNumpy).mean(axis=0)),
            'mean': np.mean(vNumpy, axis=0),
            'median': np.median(vNumpy, axis=0),
            'std': np.std(vNumpy, axis=0),
            'var': np.square(np.std(vNumpy, axis=0)),
            'min': np.min(vNumpy, axis=0),
            'max': np.max(vNumpy, axis=0)
        }
    return metrics


def print_statistics(metrics, desc='error', file=None):
    if file:
        print("samples   %d" % (metrics['pairs']), file=file)
        print("%s.rmse   %s" % (str(desc), str(metrics['rmse'])), file=file)
        print("%s.mean   %s" % (str(desc), str(metrics['mean'])), file=file)
        print("%s.median %s" % (str(desc), str(metrics['median'])), file=file)
        print("%s.std    %s" % (str(desc), str(metrics['std'])), file=file)
        print("%s.var    %s" % (str(desc), str(metrics['var'])), file=file)
        print("%s.min    %s" % (str(desc), str(metrics['min'])), file=file)
        print("%s.max    %s" % (str(desc), str(metrics['max'])), file=file)
    else:
        print("samples   %d" % (metrics['pairs']))
        print("%s.rmse   %s" % (str(desc), str(metrics['rmse'])))
        print("%s.mean   %s" % (str(desc), str(metrics['mean'])))
        print("%s.median %s" % (str(desc), str(metrics['median'])))
        print("%s.std    %s" % (str(desc), str(metrics['std'])))
        print("%s.var    %s" % (str(desc), str(metrics['var'])))
        print("%s.min    %s" % (str(desc), str(metrics['min'])))
        print("%s.max    %s" % (str(desc), str(metrics['max'])))
str()