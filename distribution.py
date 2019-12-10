from math import sqrt, log, exp, factorial, gamma, pi, cos, sin
from random import *

from utils import multiply_list

A = C = 2 ** 15 + 1
M = 2 ** 32 + 1


# BRV generator
def linear_congruential_generator(n=99999, a=A, c=C, m=M):
    for i in range(n):
        a = (c * a) % m
        yield a / m


basic_random_value = list(linear_congruential_generator())


def next_brv(n=99998):
    index = randint(0, n)
    bsv = basic_random_value[index]
    if bsv > 1:
        index = randint(0, n)
        bsv = basic_random_value[index]
    basic_random_value[index] = next(linear_congruential_generator())
    return bsv


def next_gauss_standard():
    a1 = next_brv()
    a2 = next_brv()
    n1 = sqrt(-2 * log(a1)) * cos(2 * pi * a2)
    return n1


print(next_gauss_standard())


def student(m):
    _xi_square = xi_square(m)
    gauss_standard = next_gauss_standard()
    return (gauss_standard ** 2) / (_xi_square / m)


def xi_square(m):
    snd = [next_gauss_standard() for _ in range(m)]
    return sum([i ** 2 for i in snd])


def erlang(_lambda, v):
    if v == 1:
        return exponential(1 / _lambda)

    a = [next_brv() for _ in range(v)]

    return -log(multiply_list(a)) * (1 / _lambda)


def erlang_mean(_lambda, v):
    return v / _lambda


def erlang_variance(_lambda, v):
    return v / (_lambda ** 2)


def exponential(_lambda):
    a = next_brv()
    return (-1 / _lambda) * log(a)


def erlang_distribution(l, v, x):
    if x == 0:
        x += 10 ** (-6)
    return l * ((l * x) ** (v - 1) * exp(-l * x)) / (factorial(v - 1))


def student_distribution(m, x):
    return gamma((m + 1) / 2) / (sqrt(m * pi) * gamma(m / 2) * ((1 + ((x ** 2) / m)) ** ((m + 1) / 2)))
