# encoding:utf-8
"""CART 的实现有很多种，源码在很多地方都可以找到，相信读者在阅读完前面的
部分之后，有能力看懂，并且实现出 CART 的算法，
这里使用 Scikit-Learn 中的决策树算法来看一下 CART 的预测效果，使读者有一个
直观的认识。"""

__author__ = 'eric.sun'

import matplotlib.pyplot as plt
import numpy as np
from numpy import *
from sklearn.tree import DecisionTreeRegressor

def plotfigure(X,X_test,y,yp):
    plt.figure()
    plt.scatter(X, y, c="k", label="data")
    plt.plot(X_test, yp, c="r", label="max_depth=5", linewidth=2)
    plt.xlabel("data")
    plt.ylabel("target")
    plt.title("Decision Tree Regression")
    plt.legend()
    plt.show()

x = np.linspace(-5,5,200)
print x
siny = np.sin(x) # 给出 y 与 x 的基本关系
X = mat(x).T
y = siny+np.random.rand(1,len(siny))*1.5 # 加入噪声的点集
y = y.tolist()[0]
# Fit regression model
clf = DecisionTreeRegressor(max_depth=4) # max_depth 选取最大的树深度，类似前剪枝
clf.fit(X, y)
# Predict
X_test = np.arange(-5.0, 5.0, 0.05)[:, np.newaxis]
yp = clf.predict(X_test)
plotfigure(X,X_test,y,yp)


