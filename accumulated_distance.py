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


def accumulated_distance(p_vec):
    motion_vec = np.diff(p_vec, n=1, axis=0)
    return np.cumsum(np.abs(motion_vec), axis=0)


def total_distance(p_vec):
    motion_vec = np.diff(p_vec, n=1, axis=0)
    dist_vec = np.sum(np.abs(motion_vec), axis=0)
    return np.linalg.norm(dist_vec)
