# -*- coding: utf-8 -*-
__author__ = 'eric.sun'
import sys
import os
import jieba
import pickle
from sklearn.datasets.base import Bunch

reload(sys)
sys.setdefaultencoding('utf-8')

ori_path='/others/ml_test_data/text_classification/fudan/small_ori'
#ori_path='E:\\others\\ml_test_data\\text_classification\\fudan\\small_ori'
seg_path='/others/ml_test_data/text_classification/fudan/small_seg'
bunch_data='/others/ml_test_data/text_classification/train_set.dat'
#seg_path='E:\\others\\ml_test_data\\text_classification\\fudan\\small_seg'

def save_file(path,content):
    fp=open(path,'wb')
    fp.write(content)
    fp.close()

def read_file(path):
    fp=open(path,'rb')
    content=fp.read()
    fp.close()
    return content

def segment():
    """
    将ori_path的内容，通过jieba进行分词操作
    """
    for ori_dir in os.listdir(ori_path):
        seg_dir=os.path.join(seg_path,ori_dir)
        ori_subdir_path=os.path.join(ori_path,ori_dir)
        for ori_file in os.listdir(ori_subdir_path):
            if not os.path.exists(seg_dir):
                os.mkdir(seg_dir)
            ori_content=read_file(os.path.join(ori_subdir_path,ori_file))
            #对换行符进行替换
            ori_content.replace('\r\n','').strip()
            ori_content.replace('，','')
            seg_result=jieba.cut(ori_content)
            save_file(os.path.join(seg_dir,ori_file),' '.join(seg_result))

    print 'segment finished'
#convert segment file to bunch object
def segment_bunch():
    bunch=Bunch(target_name=[],label=[],filenames=[],contents=[])    
    catelist=os.listdir(seg_path)
    bunch.target_name.extend(catelist)
    for class_dir in catelist:
        for class_file in os.listdir(os.path.join(seg_path,class_dir)):
            #print class_file
            class_file_full_path=os.path.join(seg_path,class_dir,class_file)
            bunch.label.append(class_dir)
            bunch.filenames.append(class_file_full_path)
            bunch.contents.append(read_file(class_file_full_path).strip())

    fp=open(bunch_data,'wb')
    pickle.dump(bunch,fp)
    fp.close()

    
if __name__ == '__main__':
    #segment()
    #segment_bunch()
    







