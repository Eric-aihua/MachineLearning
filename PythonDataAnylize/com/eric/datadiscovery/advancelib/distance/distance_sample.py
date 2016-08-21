# -*- coding: utf-8 -*-
__author__ = 'eric.sun'
from numpy import *

def euclidean_distance(v1,v2):
    # print v1,'\n',v1.T
    # print v2,'\n ',v2.T
    # print v1-v2
    """
    欧氏距离（ L2 范数） 是最易于理解的一种距离计算方法，源自欧氏空间中两点间的距离公式。
    :param v1:
    :param v2:
    :return:
    """
    return sqrt((v1-v2)*(v1-v2).T)

def manhattan_distance(v1,v2):
    """
    曼哈顿距离:想象你在曼哈顿要从一个十字路口开
    车到另外一个十字路口，驾驶距离是两点间的直线距离吗？显然不是，除非你能穿越
    大楼。实际驾驶距离就是这个“曼哈顿距离” (L1 范数)
    :param v1:
    :param v2:
    :return:
    """
    return sum(abs(v1-v2))

def chebyshev_d(v1,v2):
    return abs(v1-v2).max()

def cosine(vector1,vector2):
    """
    几何中夹角余弦可用来衡量两个向量方向的差异，机器学习中借用这一概念来衡
    量样本向量之间的差异
    :param v1:
    :param v2:
    """
    return dot(vector1,vector2)/(linalg.norm(vector1)*linalg.norm(vector2))


def hamming_d(v1, v2):
    """
    两个等长字符串 s1 与 s2 之间的汉明距离定义为将其中一个变为另外一个所需要
作的最小替换次数。例如字符串―1111‖与―1001‖之间的汉明距离为 2。
    :param v1:
    :param v2:
    """
    matV = mat([v1,v2])
    # print matV
    result=nonzero(matV[0]-matV[1])
    # print result
    print shape(result[0])[0]


def jaccard_s(v1, v2):
    """
    杰卡德相似系数
    两个集合 A 和 B 的交集元素在 A， B 的并集中所占的比例，称为两个集合的杰卡
    德相似系数，用符号 J(A,B)表示:
    可将杰卡德相似系数用在衡量样本的相似度上。
    :param v1:
    :param v2:
    """
    pass


def jaccard_d(v1, v2):
    """
    与杰卡德相似系数相反的概念是杰卡德距离(Jaccard distance)
    :param v1:
    :param v2:
    """
    import scipy.spatial.distance as dist
    matV = mat([v1,v2])
    print "dist.jaccard:", dist.pdist(matV,'jaccard')


def test():
    v1=mat([1,2,3])
    v2=mat([4,5,6])
    print euclidean_distance(v1,v2)
    print manhattan_distance(v1,v2)
    print chebyshev_d(v1,v2)
    print cosine(v1,v2.T)
    h1=[1,1,0,1,0,1,0,0,1]
    h2=[0,1,1,0,0,0,0,1,1]
    hamming_d(h1,h2)
    jaccard_d(v1,v2)

def sample():

    """
    使用大象、鲨鱼,苹果、梨 四种生物的重量，生命周期/保质期 作为数据，构建向量，然后计算各个向量之间的欧式距离。
    结果越大，说明两种生物的差别的就越大

    """
    test_data=[[5000,70*365],[3200,60*365],[0.25,15],[0.3,10]]
    test_data_label=['大象','鲨鱼','苹果','梨']
    for item in test_data:
        for cmp_item in test_data:
            if item!=cmp_item:
                # print item,cmp_item
                cmp_result=euclidean_distance(mat(item),mat(cmp_item))
                print "%s %s 相似值为：%s"%(str(test_data_label[test_data.index(item)]),str(test_data_label[test_data.index(cmp_item)]),int(cmp_result))



if __name__ == '__main__':
    # test()
    sample()

