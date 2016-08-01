# -*- coding: utf-8 -*-
__author__ = 'eric.sun'
import numpy as np

#初始化matrix
def init_matrix():
    zeros=np.zeros([3,5])
    ones=np.ones([3,3])
    print ones
    print zeros

#生成固定维度的matrix
def gen_random_matrix():
    rand_matrix=np.random.rand(3,4)
    print rand_matrix

#生成单位矩阵
def gen_unit_matrix():
    unit_matrix=np.eye(5)
    print unit_matrix

matrix_add=lambda m_a,m_b:m_a+m_b
matrix_sub=lambda m_a,m_b:m_a-m_b

#矩阵的相加，相减，维度必须相同
def matrix_add_sub():
    matrix1=np.ones([3,3])
    matrix2=np.eye(3)
    print matrix_add(matrix1,matrix2)
    print matrix_sub(matrix1,matrix2)

#一个整数乘以一个矩阵
def multi_matrix():
    matrix=np.eye(3)
    print 3*matrix

#矩阵和矩阵的相乘
def multi_matrix2():
    ori=[[ 3,4,2,4],[ 0,3,1,2],[ 2,6,4,3],[ 2,6,4,1]]
    ori2=[[ 1,4,3,1],[ 2,1,1,2],[ 1,2,4,3],[ 2,6,4,5]]
    ori3=2*[[ 4,3,2,3],[ 2,1,1,1]]
    #相同维度的相乘,相同坐标元素的相乘
    print np.multiply(ori,ori2)
    print '\n'
    #不同维度的相乘,相同坐标元素的相乘
    print np.multiply(np.mat(ori),ori3)
    print '\n'
    #

    print np.mat(ori)*np.mat(ori3)

def others():
    ori=[[ 3,4,2,4],[ 0,3,1,2],[ 2,6,4,3],[ 2,6,4,1]]
    matrix=np.mat(ori)
    [m,n]=np.shape(matrix)
    #得到矩阵的行列数
    print m,n
    #行切片
    print matrix[0]
    #列切片
    print matrix.T[0]





#matrix的sum操作
def matrix_sum():
    ori=[[ 3,4,2],[ 0,3,1],[ 2,6,4]]
    print ori
    matrix=np.mat(ori)
    print matrix
    print np.sum(matrix)

#matrix的次方
def power_matrix():
    ori=[[ 3,4,2],[ 0,3,1],[ 2,6,4]]
    print np.power(np.mat(ori),10)


if __name__ == '__main__':
    # init_matrix()
    # gen_random_matrix()
    # gen_unit_matrix()
    # matrix_add_sub()
    # multi_matrix()
    # matrix_sum()
    # multi_matrix2()
    # power_matrix()
    others()