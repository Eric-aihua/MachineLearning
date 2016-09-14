# -*- coding: utf-8 -*-

from numpy import *
import numpy as np
import matplotlib.pyplot as plt
import operator
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

train_data_set=[[1.0,1.1],[1.0,1.0],[0,0],[0,0.1]]
train_data_label=['A','A','B','B']
test_data_point=[0.1,0.0]

#前面的4个点已经分好类了，且各自有自己的标签，最后一个点用来判断离哪个类别更近一点
def get_train_data_set():
    test_data=np.array(train_data_set)
    labels=train_data_label
    return test_data,labels

# 夹角余弦距离公式
def cosdist(vector1,vector2):
    return dot(vector1,vector2)/(linalg.norm(vector1)*linalg.norm(vector2))

# kNN 分类器
# 测试集： testdata；训练集： trainSet；类别标签： listClasses； k:k 个邻居数
def classify(testdata, trainSet, listClasses, k):
    dataSetSize = trainSet.shape[0] # 返回样本集的行数
    distances = array(zeros(dataSetSize))
    for indx in xrange(dataSetSize): # 计算测试集与训练集之间的距离：夹角余弦
        distances[indx] = cosdist(testdata,trainSet[indx])
        # 根据生成的夹角余弦按从大到小排序,结果为索引号
        sortedDistIndicies = argsort(-distances)
    classCount={}
    for i in range(k): # 获取角度最小的前 k 项作为参考项
        # 按排序顺序返回样本集对应的类别标签
        voteIlabel = listClasses[sortedDistIndicies[i]]
        # 为字典 classCount 赋值,相同 key，其 value 加 1
        classCount[voteIlabel] = classCount.get(voteIlabel,0) + 1
    # 对分类字典 classCount 按 value 重新排序
    # sorted(data.iteritems(), key=operator.itemgetter(1), reverse=True)
    # 该句是按字典值排序的固定用法
    # classCount.iteritems()：字典迭代器函数
    # key：排序参数； operator.itemgetter(1)：多级排序
    sortedClassCount = sorted(classCount.iteritems(), key=operator.itemgetter(1), reverse=True)
    return sortedClassCount[0][0] # 返回序最高的一项

def print_data(dataset,labels,test_data_point):
    fig=plt.figure()
    ax=fig.add_subplot(111)
    #print test data point
    ax.scatter(test_data_point[0],test_data_point[1],c='red',marker='^',linewidths=0,s=300)

    for point,label in zip(dataset,labels):
        #add point
        ax.scatter(point[0],point[1],c='blue',marker='o',linewidths=0,s=300)
        #add point common
        plt.annotate("("+str(point[0])+","+str(point[1])+' '+label+")",xy = (point[0],point[1]))
    #print figure
    plt.show()


def print_test():
    train_data,train_label=get_train_data_set()
    print_data(train_data,train_label,test_data_point)

if __name__ =='__main__':
    #打印测试
    print_test()
    print classify(np.array(test_data_point),np.array(train_data_set),train_data_label,1)
