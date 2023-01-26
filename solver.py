import numpy as np
import quadpy
from scipy import integrate


def E(x):

    if 0 <= x <= 1:
        return 2
    elif 1 < x <= 2:
        return 6

    return None


def solve(n, integralAcc):  # integralAcc stands for the accuracy used in the function leggauss used for calculating integrals

    if n < 3:
        print("the n value must be greater or equal 2!")
        return

    leftBound = 0
    rightBound = 2

    # declaring matrix, and filling with zero's
    matrix = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(n):

            integral = 0

            if abs(i - j) <= 1:
                # then the integral is not equal to 0
                a = (rightBound - leftBound) * max(max(i, j) - 1, 0) / n
                b = (rightBound - leftBound) * min(min(i, j) + 1, n) / n
                deg = integralAcc

                # x-axis is being divided into n equal intervals between (-1, 1) that's why I have to map values
                # from the x array into right interval (a, b)
                x, w = np.polynomial.legendre.leggauss(deg)

                for idx, xi in enumerate(np.nditer(x)):
                    t = 0.5 * (xi + 1) * (b - a) + a
                    integral += w[idx] * (E(t) * bprime(n, leftBound, rightBound, i, t) * bprime(n, leftBound, rightBound, j, t))

                integral *= 0.5 * (b - a)

            matrix[i][j] = -E(0) * bfunc(n, leftBound, rightBound, i, 0) * bfunc(n, leftBound, rightBound, j, 0) + integral

    L = [0 for _ in range(n)]
    L[0] = -E(0) * 10 * bfunc(n, leftBound, rightBound, 0, 0) + E(0) * 3
    result = np.linalg.solve(np.array(matrix), np.array(L))

    xvalues = [i * (rightBound - leftBound) / n for i in range(n + 1)]
    yvalues = []

    for res in result:
        res += 3
        yvalues.append(res)

    yvalues.append(3)

    return {'xvalues': xvalues, 'yvalues': yvalues}


def bfunc(n, leftBound, rightBound, i, x):

    h = (rightBound - leftBound) / n
    a = n / (rightBound - leftBound)

    center = (rightBound - leftBound) * i / n
    leftB = center - h
    rightB = center + h

    if x < leftB or x > rightB:
        return 0

    elif x <= center:
        return (x - leftB) * a

    else:
        return (rightB - x) * a


def bprime(n, leftBound, rightBound, i, x):

    h = (rightBound - leftBound) / n
    a = n / (rightBound - leftBound)

    center = (rightBound - leftBound) * i / n
    leftB = center - h
    rightB = center + h

    if x < leftB or x > rightB:
        return 0

    elif x <= center:
        return a

    else:
        return -a


if __name__ == "__main__":
    print(solve(100, 100))
