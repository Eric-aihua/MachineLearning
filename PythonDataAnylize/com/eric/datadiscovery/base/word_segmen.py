# -*- coding: utf-8 -*-
__author__ = 'eric.sun'
import jieba

def word_segment():
    seg_list = jieba.cut("小明 1995 年毕业于北京清华大学", cut_all=False)
    print "Default Mode:", " ".join(seg_list) # 默认切分
    seg_list = jieba.cut("小明 1995 年毕业于北京清华大学")
    print " ".join(seg_list)
    seg_list = jieba.cut("小明 1995 年毕业于北京清华大学", cut_all=True)
    print "Full Mode:", "/ ".join(seg_list) # 全切分
    seg_list = jieba.cut_for_search("小明硕士毕业于中国科学院计算所，后在日本京都大学深造") # 搜
    #搜索引擎模式
    print "/ ".join(seg_list)
if __name__ == '__main__':
    word_segment()