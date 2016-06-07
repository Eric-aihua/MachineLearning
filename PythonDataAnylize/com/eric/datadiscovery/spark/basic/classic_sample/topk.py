# -*- encoding:utf-8-*-
from pyspark import SparkContext, SparkConf
import heapq
__author__ = 'eric.sun'
sc = SparkContext(appName='word_count')
data_file=sc.textFile("hdfs://10.5.24.137:9990/temp/2016052512/tf_00000000")
#先算出全部的wordcount
result=data_file.map(lambda x:x.split("\t")[0]).map(lambda x:(x,1)).reduceByKey(lambda x,y:x+y)

topn=10
#使用heapq.nlarges方法算出每个分区的topn,排序的key使用e[1]
par_topk=result.mapPartitions(lambda elements:heapq.nlargest(topn,elements,key=lambda e:e[1]))
#汇总每个分区的topn,并对所有分区的topn结果再次取topn,排序的key使用e[1]
final_result=heapq.nlargest(topn,par_topk.collect(),key=lambda e:e[1])
print final_result