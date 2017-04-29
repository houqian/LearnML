# -*- coding:utf-8 -*-
# @author: houqian
# @since: 17/4/28
# @desc: 练习使用statsModel

from statsmodels.tsa.stattools import adfuller as ADF
import numpy as np

print ADF(np.random.rand(100))