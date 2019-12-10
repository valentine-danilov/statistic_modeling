# from numpy import random
from random import *

import numpy as np
from test import pearson
from utils import format_test_result, report_student
from distribution import student, student_distribution, next_gauss_standard

TEST_NUMBER = 3
N = 1000
m = 4

indices = []
test_results = []
theory_means = []
theory_variances = []
real_means = []
real_variances = []

for i in range(TEST_NUMBER):
    _student_selection = np.random.standard_t(m, N)
    #_student_selection = [student(m) for _ in range(N)]
    indices.append(i + 1)
    real_mean = np.mean(np.array(_student_selection))
    real_means.append(real_mean)
    real_variances.append(np.var(np.array(_student_selection)))

    pearson_test_result = pearson(sorted(_student_selection), distr_f=student_distribution)
    test_result = format_test_result(*pearson_test_result)
    test_results.append(test_result)

headers = ["No.", "Real mean\nПолученное матожидание", "Real variance\nПолученная дисперсия",
           "Theory mean\nТеоретическое матожидание", "Theory variance\nТеоретическая дисперсия"]
rows = np.c_[indices, real_means, real_variances]
report_student("lab2_report.txt", headers, rows, test_results, N, m)
