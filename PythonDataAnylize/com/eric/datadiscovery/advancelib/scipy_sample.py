'''用scipy解非线性方程组
下面是一个实际的例子，求解如下方程组的解：
5*x1 + 3 = 0
4*x0*x0 - 2*sin(x1*x2) = 0
x1*x2 - 1.5 = 0'''
__author__ = 'Eric'
from scipy.optimize import fsolve
from math import sin,cos

def f(x):
    x0 = float(x[0])
    x1 = float(x[1])
    x2 = float(x[2])
    return [
        5*x1+3,
        4*x0*x0 - 2*sin(x1*x2),
        x1*x2 - 1.5
    ]

result = fsolve(f, [1,1,1])

print (f(result))
