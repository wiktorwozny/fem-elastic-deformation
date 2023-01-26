import numpy as np
import quadpy
from scipy import integrate


def f(x):
    return x**2


a, b = 0, 1
deg = 6
x, w = np.polynomial.legendre.leggauss(deg)

integral = 0
for i, xi in enumerate(np.nditer(x)):
    t = 0.5 * (xi + 1) * (b - a) + a
    integral += w[i] * f(t)

integral *= 0.5 * (b - a)

print(integral)

x = np.array([[1, 2], [1, 3]])
y = np.array([1, 1.5])

print(np.linalg.solve(x, y))
