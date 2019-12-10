import numpy as np
from bisect import bisect_right

epsilon = 0.05
MAX_K = 30

DELTA = {
    2: 3.841,
    3: 5.991,
    4: 7.815,
    5: 9.488,
    6: 11.070,
    7: 12.592,
    8: 14.067,
    9: 15.507,
    10: 16.919,
    11: 18.307,
    12: 19.675,
    13: 21.026,
    14: 22.362,
    15: 23.685,
    16: 24.996,
    17: 26.296,
    18: 27.587,
    19: 28.869,
    20: 30.144,
    21: 31.410,
    22: 32.671,
    23: 33.924,
    24: 35.172,
    25: 36.415,
    26: 37.652,
    27: 38.885,
    28: 40.113,
    29: 41.337,
    30: 42.557
}


def get_frequency(sorted_seq, k):
    min_el = sorted_seq[0]
    max_el = sorted_seq[-1]
    step = float((max_el - min_el) / (k + 1))
    segments = np.arange(min_el, max_el, step)
    v = [0] * k
    last_position = 0
    for i in range(k):
        position = bisect_right(sorted_seq, segments[i + 1])
        v[i] = position - last_position
        last_position = position
    return v, segments


def get_probabilities(segments, f):
    k = len(segments)
    p = [0] * k
    for i in range(k - 1):
        p[i] = f(1, segments[i + 1]) - f(1, segments[i])
    return p


def pearson(sorted_seq, distr_f):
    n = len(sorted_seq)
    k = MAX_K
    v, segments = get_frequency(sorted_seq, k)
    p = get_probabilities(segments, distr_f)
    delta = DELTA[k]
    value = sum([(v[i] - n * p[i]) ** 2 / (n * p[i]) for i in range(k)])
    return value, delta, k
