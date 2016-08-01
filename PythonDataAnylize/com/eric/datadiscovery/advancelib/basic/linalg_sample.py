# -*- coding: utf-8 -*-
__author__ = 'eric.sun'
import numpy as np

#n阶方阵的行列式
def det():
    ori=[[2,7],[2,3]]
    matrix=np.mat(ori)
    print np.linalg.det(matrix)
#方阵的逆,AB=BA=E ,则AB互逆
def inv():
    ori=[[2,7,3],[2,3,4],[2,5,4]]
    matrix=np.mat(ori)
    result=np.linalg.inv(matrix)
    print result

    print result*matrix
    print matrix*result

#方阵的对称,对于任何方形矩阵X，X+XT是对称矩阵
def symmetry():
    ori=[[2,7,3,7],[2,3,4,6],[2,5,4,2],[1,1,1,1]]
    matrix=np.mat(ori)
    t_matrix=matrix.T
    print matrix+t_matrix

#矩阵的秩
def matrix_rank():
    ori=[[2,7,3,7],[2,3,4,6],[2,5,4,2],[1,1,1,1]]
    matrix=np.mat(ori)
    print np.linalg.matrix_rank(matrix)

if __name__ == '__main__':
    # det()
    # inv()
    # symmetry()
    matrix_rank()

