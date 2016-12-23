# encoding:utf-8
__author__ = 'eric.sun'
"""推荐系统"""

# from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import numpy as np

#加载testdata/ml-100/u.data 的数据
def load_rating_data():
        with open('E:\\Sourcecode\\github\\MachineLearning\\PythonDataAnylize\\testdata\\ml-100k\\u.data_2') as f:
            for line in f:
                yield line.split('\t')[:3]

def load_user_data():
        with open('E:\\Sourcecode\\github\\MachineLearning\\PythonDataAnylize\\testdata\\ml-100k\\u.user') as f:
            for line in f:
                yield line.split('|')[0]
def load_movie_data():
        with open('E:\\Sourcecode\\github\\MachineLearning\\PythonDataAnylize\\testdata\\ml-100k\\u.item') as f:
            for line in f:
                yield line.split('|')[0]
def gen_key(row,col):
    return str(row)+'_'+str(col)

def load_matrix():
    rating_data=load_rating_data()
    user_movie_map={}
    for line in rating_data:
        if line:
            #key使用userid_movieid的格式_
            rating_key=gen_key(line[0],line[1])
            user_movie_map[rating_key]=line[2]
    user_data=list(load_user_data())
    item_data=list(load_movie_data())
    rating_matrix=[[0 for col in item_data ]for row in user_data]
    for user_id in user_data:
        for movie_id in item_data:
            tmp_key=gen_key(user_id,movie_id)
            if user_movie_map.has_key(tmp_key):
                print tmp_key,user_movie_map[tmp_key]
                rating_matrix[int(user_id)-1][int(movie_id)-1]=user_movie_map[tmp_key]
    return rating_matrix


def load_kmeans_result():
    matrix=load_matrix()
    X = np.array(matrix)
    plt.figure(figsize=(12, 12))
    kmeans = KMeans(n_clusters=10, random_state=0).fit(X)
    y_pred = kmeans.predict(X)
    clusters = kmeans.cluster_centers_
    plt.scatter(X[:, 0], X[:, 1], c=y_pred)
    plt.scatter(clusters[:, 0], clusters[:, 1], c='red', marker='d')
    plt.title("Incorrect Number of Blobs")
    plt.show()





def recommand_by_distance(result):
    pass


def recommand_by_svd(result):
    pass


if __name__ == '__main__':
    # 使用K-Means对数据进行分类
    result=load_kmeans_result()
    # 对聚类后的结果使用领域算法进行推荐
    recommand_by_distance(result)
    # 对聚类后的结果使用SVD算法进行推荐
    recommand_by_svd(result)



