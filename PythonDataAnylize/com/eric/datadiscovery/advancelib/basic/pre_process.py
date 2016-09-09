# -*- coding: utf-8 -*-
from numpy import *
import os
import logging
import cPickle as pickle

def file2matrix(path,delimiter):
    """
    convert a file to matrix
    :param path:
    :param delimiter:
    """
    if os.path.isfile(path):
        fp=open(path)
        content=fp.read()
        file_lines=content.splitlines()
        data_list=[line.split(delimiter) for line in file_lines]
        return mat(data_list)
    else:
        logging.info("path not a file")
        return mat([])

def persist(data,file):
    """
    将data数据序列化到file文件中
    :param data:
    :param file:
    """
    fp=open(file,'wb')
    pickle.dump(data,fp)

def load(file):
    """
    从file文件中加载数据
    :param file:
    """
    fp=open(file,'rb')
    return pickle.load(fp)


if __name__ == '__main__':
    result =file2matrix('/home/eric/sourcecode/git/MachineLearning/PythonDataAnylize/testdata/ml-100k/u.data','\t')
    # print result
    print 'original result:',shape(result)
    persist_file='./data'
    persist(result,persist_file)
    data=load(persist_file)
    print 'from file data:',shape(data)

