# -*- coding: utf-8 -*-
__author__ = 'eric.sun'
import sys
import os
import jieba
import pickle
from sklearn.datasets.base import Bunch
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB




reload(sys)
sys.setdefaultencoding('utf-8')

ori_path='/others/ml_test_data/text_classification/fudan/small_ori'
#ori_path='E:\\others\\ml_test_data\\text_classification\\fudan\\small_ori'
seg_path='/others/ml_test_data/text_classification/fudan/small_seg'
train_data= '/others/ml_test_data/text_classification/train_set.dat'

#test_file 是用来被预测的数据，拷贝自sport450/10201.txt 以及medicine204/7173.txt,
# 以及一篇来自qq体育的新闻：http://sports.qq.com/a/20160828/014734.htm（放在medicine下）
#    一篇来自里约奥运会的新闻：
# ，结构如下
# .
# ├── medicine204
# │   ├── 7173.txt
# │   └── qq_news.txt
# └── sport450
#     ├── 10201.txt
#     └── rio_olympic.txt



test_file_path='/others/ml_test_data/text_classification/test_txt'
test_data= '/others/ml_test_data/text_classification/test_set.dat'

test_space_path= '/others/ml_test_data/text_classification/test_space.dat'
tf_idf_space_data='/others/ml_test_data/text_classification/tf_idf_space.dat'
stop_words_path='/others/ml_test_data/text_classification/stop_word.txt'
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

def save_object(path,content):
    fp=open(path,'wb')
    pickle.dump(content,fp)
    fp.close()

def read_object(path):
    fp=open(path,'rb')
    object=pickle.load(fp)
    fp.close()
    return object

#（1）对词库数据文件进行分词
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
#将分词数据转换成文本向量
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

    save_object(train_data, bunch)
#停词对象
def load_stop_words():
    return read_file(stop_words_path).splitlines()

#（2）生成tf_idf 词向量空间
def gen_tf_idf_space():
    bunch=read_object(train_data)
    tf_idf_space=Bunch(target_name=bunch.target_name,label=bunch.label,filenames=bunch.filenames,vocabulary={})

    vectorizer=TfidfVectorizer(stop_words=load_stop_words(),sublinear_tf = True,max_df = 0.5)
    transformer=TfidfTransformer()

    tf_idf_space.tdm=vectorizer.fit_transform(bunch.contents)
    tf_idf_space.vocabulary=vectorizer.vocabulary_
    save_object(tf_idf_space_data,tf_idf_space)
    # print tf_idf_space

#（3）生成测试数据的data文件
def gen_test_data():
    bunch = Bunch(target_name=[], label=[], filenames=[], contents=[])
    catelist = os.listdir(test_file_path)
    bunch.target_name.extend(catelist)
    for class_dir in catelist:
        for class_file in os.listdir(os.path.join(test_file_path, class_dir)):
            # print class_file
            class_file_full_path = os.path.join(test_file_path, class_dir, class_file)
            bunch.label.append(class_dir)
            bunch.filenames.append(class_file_full_path)
            bunch.contents.append(read_file(class_file_full_path).strip())

    save_object(test_data, bunch)


#（4）使用多项贝叶斯进行预测
def execute_NM_predict():
    test_bunch=read_object(test_data)

    test_space=Bunch(target_name=test_bunch.target_name, label=test_bunch.label, filenames=test_bunch.filenames, tdm=[], vocabulary = {})

    tf_idf_bunch=read_object(tf_idf_space_data)
    vectorizer = TfidfVectorizer(stop_words=load_stop_words(), sublinear_tf=True, max_df=0.5,vocabulary=tf_idf_bunch.vocabulary)
    transformer = TfidfTransformer()

    test_space.tdm = vectorizer.fit_transform(test_bunch.contents)
    test_space.vocabulary = tf_idf_bunch.vocabulary

    clf=MultinomialNB(alpha=0.001).fit(tf_idf_bunch.tdm,tf_idf_bunch.label)
    #预测结果
    predicted=clf.predict(test_space.tdm)
    #对结果进行更加友好的打印
    for label,file_name,excect_cate in zip(test_bunch.label,test_bunch.filenames,predicted):
        print file_name,' 实际类别：',label,' 预测类别：',excect_cate

    # print predicted




if __name__ == '__main__':
    # segment()
    # segment_bunch()
    # load_stop_words()
    # gen_tf_idf_space()
    gen_test_data()
    execute_NM_predict()


    







