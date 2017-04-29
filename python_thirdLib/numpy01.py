# -*- coding:utf-8 -*-
# @author: houqian
# @since: 17/4/27
# @desc: 练习numpy的基本用法

import numpy as np

a = np.array([2, 0, 1, 5])
print (a)
print (a[:3])  # 引用前三个数字 切片
print (a.min())
a.sort()  # 对a排序，直接操作a的元素
b = np.array([[1, 2, 3], [4, 5, 6]])
print 'array b：%s' % (b)
print (b * b)  # 输出数组的平方阵

