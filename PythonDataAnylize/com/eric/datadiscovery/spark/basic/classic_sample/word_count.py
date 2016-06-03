# -*- encoding:utf-8-*-
from pyspark import SparkContext, SparkConf

__author__ = 'eric.sun'
conf = SparkConf().setAppName("word_count")
#sc = SparkContext(master="spark://10.5.24.137:7077",appName= "word_count")
sc = SparkContext(conf)
batch_out=sc.textFile("hdfs://10.5.24.137:9990/temp/batch.out")
#rdd=sc.parallelize(batch_out)
error_rdd=batch_out.filter(lambda x:"ERR" in x)
error_rdd.count()

