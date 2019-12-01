import numpy as np
from math import sqrt

KOLMOGOROV_DELTA = 1.36


def kolmogorov(sorted_seq):
    """
    Kolmogorov–Smirnov test
    :param sorted_seq: model distribution on sorted random sequence
    :return: test value, test delta
    """
    n = len(sorted_seq)
    test_seq = np.array([float(i + 1) / n for i in range(n)])
    max_diff = max(list(map(abs, test_seq - sorted_seq)))
    value = sqrt(n) * max_diff
    return value, KOLMOGOROV_DELTA
