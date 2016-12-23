# encoding:utf-8
__author__ = 'eric.sun'
"""推荐系统"""

from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import numpy as np

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
    matrix=[[0.238,0,0.1905,0.1905,0.1905,0.1905],[0,0.177,0,0.294,0.235,0.294],[0.2,0.16,0.12,0.12,0.2,0.2]]
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


def recommand_by_distance():
    import sys
    sys.path.append('/root/source/git/MachineLearning/PythonDataAnylize/com/eric/datadiscovery')
    from text_classification.knn_main import classify
    dataset=load_test_data();
    data_point=[0.2174,0.2174,0.1304,0,0.2174,0.2174]
    labels=['B','C','D']
    print classify(np.array(data_point),np.array(dataset),labels,2)


def recommand_by_svd():
    pass


if __name__ == '__main__':
    # 使用K-Means对数据进行分类
    # result = load_kmeans_result()

    # 对聚类后的结果使用领域算法进行推荐
    recommand_by_distance()
    # 对聚类后的结果使用SVD算法进行推荐
    recommand_by_svd()



