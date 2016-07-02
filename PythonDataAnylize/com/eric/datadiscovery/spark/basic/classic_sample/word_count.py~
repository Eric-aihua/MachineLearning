# -*- encoding:utf-8-*-
from pyspark import SparkContext, SparkConf

__author__ = 'eric.sun'
sc = SparkContext(appName='word_count')
#该数据文件的字段用\t风格，第一列为IP,需要统计每个IP在文件中出现的行数
data_file=sc.textFile("hdfs://10.5.24.137:9990/temp/2016052512/tf_00000000")
#1,先对文件的行按照\t进行分割，并提取第一个字段IP
#2,将每个提取到的IP转换成(IP,1)的格式
#3，把所有的(IP,1)的数据使用reduceBy进行统计操作
#4,将结果打印出来
result=data_file.map(lambda x:x.split("\t")[0]).map(lambda x:(x,1)).reduceByKey(lambda x,y:x+y)
def printx(x):print x
result.foreach(lambda x:printx(x))

