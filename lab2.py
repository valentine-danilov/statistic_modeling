from distribution import student
from test import kolmogorov
from utils import format_test_result
from numpy import random

N = 1000
m = 1

student_result = random.standard_t(m, N)
print(sorted(student_result))

k = kolmogorov(sorted(student_result))
print(format_test_result(*k))
