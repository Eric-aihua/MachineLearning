# -*- coding: utf-8 -*-
__author__ = 'eric.sun'
import sys
import os
import jieba

def save_file(path,content):
    fp=open(path,'wb')
    fp.write(content)
    fp.close()

def read_file(path):
    fp=open(path,'rb')
    content=fp.read()
    fp.close()
    return content




