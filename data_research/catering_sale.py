# -*- coding:utf-8 -*-
# @author: houqian
# @since: 17/4/29
# @desc:

import pandas as pd

catering_sale = '/Users/pen/Downloads/Python数据分析与挖掘实战/图书配套数据、代码/chapter3/demo/data/catering_sale.xls'
data = pd.read_excel(catering_sale, index_col=u'日期')  # 读取数据，指定「日期」列为索引列

import matplotlib.pyplot as plt  # 导入图像库

plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

plt.figure()  # 建立图像
p = data.boxplot(return_type = 'dict')  # 画箱线图，直接使用dataFrame的方法
x = p['fliers'][0].get_xdata()
y = p['fliers'][0].get_ydata()
y.sort

for i in range(len(x)):
    if i > 0:
        plt.annotate(y[i], xy=(x[i], y[i]), xytext=(x[i] + 0.05 - 0.8 / (y[i] - y[i - 1]), y[i]))
    else:
        plt.annotate(y[i], xy=(x[i], y[i]), xytext=(x[i] + 0.08, y[i]))

plt.show()