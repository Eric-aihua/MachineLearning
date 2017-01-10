__author__ = 'eric.sun'
import numpy as np
import matplotlib.pyplot as plt

from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs
import random

plt.figure(figsize=(12, 12))

# n_samples = 1500
#random_state = 170
#X, y = make_blobs(n_samples=n_samples, random_state=random_state)

<<<<<<< HEAD
arrays=[[random.randint(1,100),random.randint(1,100)] for i in range(100)]
=======
arrays = [[random.randint(1, 100), random.randint(1, 100)] for i in range(100)]
>>>>>>> 5f93ed73afa17fa09511603b759e8ad9b939c64c
#X = np.array([[1, 2], [1, 3], [1, 1],[4, 3], [4, 4], [3, 5]])
X = np.array(arrays)

#y_pred = KMeans(n_clusters=5, random_state=random_state).fit_predict(X)

kmeans = KMeans(n_clusters=4, random_state=0).fit(X)
y_pred = kmeans.predict(X)
clusters = kmeans.cluster_centers_
plt.scatter(X[:, 0], X[:, 1], c=y_pred)
plt.scatter(clusters[:, 0], clusters[:, 1], c='red', marker='d')
plt.title("Incorrect Number of Blobs")
plt.show()
