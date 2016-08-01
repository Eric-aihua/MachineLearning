# -*- coding: utf-8 -*-
import random
import numpy as np
import matplotlib.pyplot as plt
__author__ = 'eric.sun'

#产生数据点
def gen_points():
    points=[]
    for index in range(100):
        points.append([random.randint(1,100),random.randint(1,100)])
    # print points
    return points

#利用数据点，绘制图
def gen_point_graph(data_points):
    #生成矩阵，并转置
    data_mat=np.mat(data_points).T
    # print data_mat
    #绘制散点图
    plt.scatter(data_mat[0],data_mat[1],c='red',marker='o')

#根据线性方程，生成直线
def gen_line():
    #生成X轴的数据点
    X=np.linspace(start=1,stop=100,num=100)
    print X
    #生产Y的映射函数
    Y=2*X+3
    plt.plot(X,Y)






gen_point_graph(gen_points())
gen_line()
plt.show()

