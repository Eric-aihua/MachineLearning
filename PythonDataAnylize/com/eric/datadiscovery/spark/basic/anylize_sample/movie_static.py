# -*- coding: utf-8 -*-
from pyspark import SparkContext
import matplotlib.pyplot as plt
import numpy as np

logFile = "/opt/talas/ml-100k/u.item"  # Should be some file on your system
sc = SparkContext("local", "MOVIE Statics")
#1|Toy Story (1995)|01-Jan-1995||http://us.imdb.com/M/title-exact?Toy%20Story%20(1995)|0|0|0|1|1|1|0|0|0|0|0|0|0|0|0|0|0|0|0
movie_data = sc.textFile(logFile).cache()
sc.parallelize()
movie_fields=movie_data.map(lambda line:line.split("|"));
movie_fields.cache()

def convert_year(original_year):
	try:
		return int(original_year[-4:])
	except:
		return 1900

#打印电影的发行时间分布情况
def print_movie_year_dis():
	years=movie_fields.map(lambda fields:fields[2]).map(lambda year:convert_year(year))
	years_filter=years.filter(lambda year:year!=1900)
	years_map=years_filter.map(lambda year:2010-year).countByValue()
	years_keys=years_map.keys()
	years_values=years_map.values();
	plt.hist(years_values,bins=years_keys,color='lightblue',normed=True)
	#below code just nessary by spark-submit
	plt.show()
	fig=plt.gcf()
	fig.set_size_inches(16,10)

if __name__=="__main__":
	print_movie_year_dis()


