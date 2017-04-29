# -*- coding:utf-8 -*-
# @author: houqian
# @since: 17/4/27
# @desc: 练习使用matplotlib

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-4, 10, num=1000)  # 作图的变量自变量  创建一个等差数列 start: 0, stop: 10, numCnt: 1000
# print x
y = np.sin(x) + 1  # 因变量
# print y
z = np.cos(x ** 2) + 1  # 因变量
# print z

plt.figure(figsize=(8, 4))  # 设置图像大小
plt.plot(x, y, label='$\sin x+1$', color='red', linewidth=2)  # 设置标签 线条颜色 线条粗细
plt.plot(x, z, 'b--', label='$cos x^2+1$')

# 比葫芦画个抛物线
y = 0.5 * x ** 2
plt.plot(x, y, label=r'$\frac{1}{2} x ^ 2$', color='green', linewidth=2)

y = x ** 0.5
plt.plot(x, y, label=r'$x ^ \frac{1}{2}$', color='blue', linewidth=2)

plt.grid(True)
plt.xlabel('Time(s)')  # x轴名称
plt.ylabel('Volt')  # y轴名称
plt.title('A sample Example')  # 标题
plt.ylim(0, 2.2)  # 显示y轴范围
plt.legend()  # 显示图例
plt.show()  # 显示作图结果

