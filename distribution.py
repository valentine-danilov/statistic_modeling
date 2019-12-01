from math import sqrt, erf, log, exp, factorial
from random import *

A = C = 2 ** 15 + 1
M = 2 ** 32 + 1


def multiplyList(myList):
    # Multiply elements one by one
    result = 1
    for x in myList:
        result = result * x
    return result


# BRV generator
def linear_congruential_generator(n=9999, a=A, c=C, m=M):
    for i in range(n):
        a = (c * a) % m
        yield a / m


basic_random_value = list(linear_congruential_generator())


def next_brv(n=9998):
    bsv = basic_random_value[randint(0, n)]
    while bsv >= 1:
        bsv = basic_random_value[randint(0, n)]
    return bsv


def next_gauss_standard():
    return sum([random() for _ in range(12)]) - 6


def student(m):
    snd = [next_gauss_standard() for _ in range(m + 1)]
    e0 = snd[0]
    e1_m = snd[1:]
    _sum = 0
    for i in e1_m:
        _sum += i ** 2
    # res = e0 / sqrt(sum([i ** 2 for i in e1_m]) / m)
    res = e0 / sqrt(_sum / m)
    #print("e0: {}, e1_m: {}, sum: {}, res: {}".format(e0, e1_m, _sum, sqrt(_sum)))
    return res


def erlang(_lambda, v):
    if v == 1:
        return exponential(1 / _lambda)

    a = [next_brv() for _ in range(v)]

    return -log(multiplyList(a)) * (1 / _lambda)


def erlang_mean(_lambda, v):
    return v / _lambda


def erlang_variance(_lambda, v):
    return v / (_lambda ** 2)


def exponential(_lambda):
    a = next_brv()
    return (-1 / _lambda) * log(a)


def mmg(b, c, k, n):
    """
    MacLaren-Marsaglia generator (MMG)
    """
    v = b[:k]
    for i in range(n):
        s = int(c[i] * k)
        yield v[s]
        v[s] = b[i + k]


def erlang_distribution(l, v, x):
    if x == 0:
        x += 10 ** (-6)
    return l * ((l * x) ** (v - 1) * exp(-l * x)) / (factorial(v - 1))


# Gauss
def get_next_standard_gauss():
    return sum([random() for _ in range(12)]) - 6


def get_next_gauss(m, s):
    return m + s * get_next_standard_gauss()


def gauss(m, s, n):
    """
    N(m, s^2)
        :param m: mean
        :param s: dispersion
        :param n: size
    """
    for _ in range(n):
        yield get_next_gauss(m, s)


def gauss_distribution(m, s, x):
    return 0.5 * (1 + erf((x - m) / (sqrt(2) * s)))
