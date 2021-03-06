# -*- coding:utf-8 -*-
# @author: houqian
# @since: 17/4/28
# @desc: 练习使用scikit-learn

from sklearn import datasets  # 导入数据集

iris = datasets.load_iris()  # 加载数据集
print (iris.data.shape)  # 查看数据集大小

from sklearn import svm  # 导入svm模型

clf = svm.LinearSVC()  # 建立线性svm分类器
clf.fit(iris.data, iris.target)  # 用数据训练模型
clf.predict([[5.0, 3.6, 1.3, 0.25]])  # 训练好模型之后，输入新的数据进行预测
print clf.coef_  # 查看训练好模型的参数
