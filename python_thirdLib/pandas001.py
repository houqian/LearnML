# -*- coding:utf-8 -*-
# @author: houqian
# @since: 17/4/28
# @desc: 练习使用pandas

import pandas as pd

s = pd.Series([1, 2, 3], index=['a', 'b', 'c'])
d = pd.DataFrame([[1, 2, 3], [4, 5, 6]], columns=['a', 'b', 'c'])
d2 = pd.DataFrame(s)
print d
print d.sum()
print d.max
print d.head()  # 预览前五行数据
print d.describe()  # 数据基本统计量

# pd.read_excel('data.xls')
# pd.read_csv('data.csv', encoding='utf-8')
