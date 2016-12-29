# encoding:utf-8
__author__ = 'eric.sun'
"""推荐系统"""

from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import numpy as np
from numpy import *
import operator

# 加载testdata/ml-100/u.data 的数据
def load_rating_data():
    with open('/root/source/git/MachineLearning/PythonDataAnylize/testdata/ml-100k/u.data') as f:
        for line in f:
            yield line.split('\t')[:3]


def load_user_data():
    with open('/root/source/git/MachineLearning/PythonDataAnylize/testdata/ml-100k/u.user') as f:
        for line in f:
            yield line.split('|')[0]


def load_movie_data():
    with open('/root/source/git/MachineLearning/PythonDataAnylize/testdata/ml-100k/u.item') as f:
        for line in f:
            yield line.split('|')[0]


def gen_key(row, col):
    return str(row) + '_' + str(col)


def load_matrix():
    rating_data = load_rating_data()
    user_movie_map = {}
    for line in rating_data:
        if line:
            #key使用userid_movieid的格式_
            rating_key = gen_key(line[0], line[1])
            user_movie_map[rating_key] = line[2]
    user_data = list(load_user_data())
    item_data = list(load_movie_data())
    rating_matrix = [[0 for col in item_data] for row in user_data]
    for user_id in user_data:
        for movie_id in item_data:
            tmp_key = gen_key(user_id, movie_id)
            if user_movie_map.has_key(tmp_key):
                #print tmp_key,user_movie_map[tmp_key]
                rating_matrix[int(user_id) - 1][int(movie_id) - 1] = user_movie_map[tmp_key]

    # 对数据进行归一化处理
    for row,line in enumerate(rating_matrix):
        sum_raging = sum([int(x) for x in line])
        #print sum_raging
        for col,element in enumerate(line):
            #print rating_matrix[row][col]
            rating_matrix[row][col] = float(element)/float(sum_raging)
    return rating_matrix

def load_test_data():
    matrix=[[0.238,0,0.1905,0.1905,0.1905,0.1905],[0,0.177,0,0.294,0.235,0.294],[0.2,0.16,0.12,0.12,0.2,0.2],[0.2,0.16,0.12,0.12,0.2,0.1]]
    return matrix
def load_kmeans_result():
    # 使用movie的数据进行验证
    #matrix = load_matrix()

    #使用测试数据进行验证
    matrix = load_test_data()
    #X=matrix
    X = np.array(matrix)
    plt.figure(figsize=(120, 120))
    kmeans = KMeans(n_clusters=10, random_state=0).fit(X)
    y_pred = kmeans.predict(X)
    clusters = kmeans.cluster_centers_
    plt.scatter(X[:, 0], X[:, 1], c=y_pred,s=50)
    plt.scatter(clusters[:, 0], clusters[:, 1], c='red', marker='d',s=100)
    plt.title("Incorrect Number of Blobs")
    plt.show()


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

def recommand_by_distance():
    dataset=load_test_data();
    data_point=[0.2174,0.2174,0.1304,0,0.2174,0.2174]
    labels=['B','C','D','E']
    print classify(np.array(data_point),np.array(dataset),labels,2)

def comsSim(vecA,vecB):
    eps=1.0e-6
    a=vecA[0]
    b=vecB[0]
    return dot(a,b)/((np.linalg.norm(a)*np.linalg.norm(b))+eps)

def recommand_by_svd():
    r=1
    dataset=np.mat(load_test_data())
    data_point=np.mat([[0.2174,0.2174,0.1304,0,0.2174,0.2174]])
    m,n=np.shape(dataset)
    limit=min(m,n)
    if r>limit:r=limit
    U,S,VT=np.linalg.svd(dataset.T)
    V=VT.T
    Ur=U[:,:r]
    Sr=np.diag(S)[:r,:r]
    Vr=V[:,:r]
    testresult=data_point*Ur*np.linalg.inv(Sr)
    resultarray=array([comsSim(testresult,vi) for vi in Vr])
    descindx=argsort(-resultarray)[:1]
    print descindx
    print resultarray



if __name__ == '__main__':
    # 使用K-Means对数据进行分类
    # result = load_kmeans_result()

    # 使用领域算法进行推荐
    recommand_by_distance()
    # 使用SVD算法进行推荐
    recommand_by_svd()

