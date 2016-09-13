# -*- coding: utf-8 -*-

from numpy import *
import numpy as np
import matplotlib.pyplot as plt
import operator
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

def get_test_data_set():
    test_data=np.array([[1.0,1.1],[1.0,1.0],[0,0],[0,0.1]])
    labels=['A','A','B','B']
    return test_data,labels 
def print_data(dataset,labels):
        



if __name__ =='__main__':
    test_data,test_label=get_test_data_set()
    print_data(test_data,test_label)
