# encoding:utf-8

import numpy as np
from com.eric.datadiscovery.advancelib.distance.distance_sample import euclidean_distance


def file_to_matrix(path, delimiter=' '):
    f = open(path)
    record_list = []
    for line in f:
        if line.strip():
            record_list.append(map(eval,line.split(delimiter)))
    return np.mat(record_list)


# generate a random cluster centers
def random_centers(dataset,k):
    n=np.shape(dataset)[1]
    cluster_centers=np.mat(np.zeros((k,n)))
    for col in xrange(n):
        mincol=min(dataset[:,col])
        maxcol=max(dataset[:,col])
        cluster_centers[:,col]=np.mat(mincol+float(maxcol-mincol)*np.random.rand(k,1))
    return cluster_centers

if __name__ == '__main__':
    matrix=file_to_matrix('./kmeans_data.txt')
    m=np.shape(matrix)[0]
    random_count=3
    # print matrix
    random_centers=random_centers(matrix,random_count)
    flag=True
    counter=[]
    # used to save distance result
    cluster_dist=np.mat(np.zeros((m,2)))
    # print cluster_dist
    for i in range(m):
        dist_list=[euclidean_distance(random_centers[random_index   ,:],matrix[i,:]) for random_index in range(random_count)]
        min_dist=min(dist_list)
        min_dist_index=dist_list.index(min_dist)
        if cluster_dist[i,0]!=min_dist_index:
            flag=True

        cluster_dist[i,:]=min_dist_index,min_dist
        print cluster_dist