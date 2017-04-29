# -*- coding:utf-8 -*-
# @author: houqian
# @since: 17/4/27
# @desc: 练习使用scipy

from scipy.optimize import fsolve  # 求解方程组函数


def f(x):
    x1 = x[0]
    x2 = x[1]
    return [2 * x1 - x2 ** 2 - 1, x1 ** 2 - x2 - 2]


result = fsolve(f, [1, 1])  # 输入初值[1, 1]并求解
print (result)

# --------------------------------------
from scipy import integrate


def g(x):
    return (1 - x ** 2) ** 0.5


pi_2, err = integrate.quad(g, -1, 1)  # 积分结果和误差
print (pi_2 * 2)  # 由微积分知识知道积分结果位圆周率pi的一半
