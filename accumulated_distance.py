import numpy as np


def accumulated_distance(p_vec):
    motion_vec = np.diff(p_vec, n=1, axis=0)
    return np.cumsum(np.abs(motion_vec), axis=0)


def total_distance(p_vec):
    motion_vec = np.diff(p_vec, n=1, axis=0)
    dist_vec = np.sum(np.abs(motion_vec), axis=0)
    return np.linalg.norm(dist_vec)
