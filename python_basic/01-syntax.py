# -*- coding:utf-8 -*-
# @author: houqian
# @since: 17/4/22
# @desc:


'''
# 循环

s = 0
for k in range(1010):
    s = s + k
print s
'''

'''
# 在区间 不在区间
s = 0
if s in range(4):
    print u's在0，1，2，3中'
if s not in range(1, 4, 1):
    print u's不在1，2，3中'
'''


def add2(x):
    return x + 2


print add2(1)


def add3(x=0, y=0):  # 定义函数，同时定义函数的默认值
    return x + y


print add3(1, 2)


def add4(x=0, y=0):
    return [x + 2, y + 2]  # 返回值是一个列表


print add4(1, 2)


def add5(x=0, y=0):
    return x + 2, y + 2  # 双重返回


print add5(1, 2)

a, b = add5(1, 2)
print '%d, %d' % (a, b)

f = lambda x: x + 2  # 定义函数 f(x) = x+2
g = lambda x, y: x + y  # 定义函数 g(x, y) = x+y
print f(1)
print g(1, 2)
