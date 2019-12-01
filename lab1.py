from distribution import *
from utils import *
import numpy as np

# parameters
v = [1, 2, 3]
lambdas = [1]
n = 15
N = 10000

erlang_theory_means = []
erlang_theory_variances = []
erlang_real_means = []
erlang_real_variances = []

for _v in v:
    for _lambda in lambdas:
        _selection = np.array([erlang(_lambda, _v) for _ in range(N)])
        _mean = np.mean(_selection)
        _variance = np.var(_selection)
        erlang_real_means.append(_mean)
        erlang_real_variances.append(_variance)
        erlang_theory_means.append(erlang_mean(_lambda, _v))
        erlang_theory_variances.append(erlang_variance(_lambda, _v))

headers = ["v", "Real mean\nПолученное матожидание", "Real variance\nПолученная дисперсия",
           "Theory mean\nТеоретическое матожидание", "Theory variance\nТеоретическая дисперсия"]
rows = np.c_[v, erlang_real_means, erlang_real_variances, erlang_theory_means, erlang_theory_variances]
report_erlang("output1.txt", headers, rows, N, lambdas[0])
