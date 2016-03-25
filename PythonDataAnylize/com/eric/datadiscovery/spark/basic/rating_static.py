# -*- coding: utf-8 -*-
from pyspark import SparkContext
import matplotlib.pyplot as plt
import numpy as np

logFile = "/opt/talas/ml-100k/u.data"  # Should be some file on your system
sc = SparkContext("local", "Data Statics")
#196	242	3	881250949
rating_data = sc.textFile(logFile).cache()
rating_fields=rating_data.map(lambda line:line.split("\t"));
rating_fields.cache()

#使用stats得到rate的统计信息
def get_stats_by_func():
	rating_value=rating_fields.map(lambda rating:int(rating[2]));
	print rating_value.stats();

#显示年龄的分布情况
def get_stats_by_dig():
	rating_value=rating_fields.map(lambda rating:int(rating[2]));
	rating_map=rating_value.countByValue()
	rating_keys=rating_map.keys()
	rating_values=rating_map.values();
	x_elements=np.array(rating_keys)
	y_elements=np.array([float(x) for x in rating_values])

	pos=np.arange(len(x_elements))
	width=2.0
	
	ax=plt.axes()
	ax.set_xticks(pos+(width/2))
	ax.set_xticklabels(x_elements)
	plt.bar(pos,y_elements,width,color='lightblue')
	plt.show()
	fig=plt.gcf()
	fig.set_size_inches(16,10)
	

if __name__=="__main__":
	get_stats_by_dig()


