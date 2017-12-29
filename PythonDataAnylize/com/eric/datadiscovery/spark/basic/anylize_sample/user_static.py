# -*- coding: utf-8 -*-
from pyspark import SparkContext
import matplotlib.pyplot as plt
import numpy as np

logFile = "E:\\Sourcecode\\github\\MachineLearning\\PythonDataAnylize\\testdata\\ml-100k\\u.user"  # Should be some file on your system
sc = SparkContext("local", "User Statics")
#Data Sample:1|24|M|technician|8571
user_data = sc.textFile(logFile).cache()
user_fields=user_data.map(lambda line:line.split("|"));
user_fields.cache()

def print_basic_info():
	#打印出基本的数据情况
	num_users=user_fields.map(lambda fields:fields[0]).count()
	num_age=user_fields.map(lambda fields:fields[1]).distinct().count()
	num_gender=user_fields.map(lambda fields:fields[2]).distinct().count()
	num_occupation=user_fields.map(lambda fields:fields[3]).distinct().count()
	num_zipcode=user_fields.map(lambda fields:fields[4]).distinct().count()
	print "Users: %d  Ages: %d Genders: %d Occupations: %d ZipCodes: %d" % (num_users,num_age,num_gender,num_occupation,num_zipcode)

#按照职业的情况打印出分布图
def print_occuration_info():

	#使用常规方法统计每个职业的人数
	count_by_occu=user_fields.map(lambda fields:(fields[3],1)).reduceByKey(lambda x,y:x+y).collect();
	#使用countByValue方法统计每个职业的人数
	#count_by_occu=user_fields.map(lambda fields:fields[3]).countByValue()
	x_item=np.array([occu[0] for occu in count_by_occu])
	#x_item=np.array([occu for occu in count_by_occu])
	y_item=np.array([occu[1] for occu in count_by_occu])
	#y_item=np.array([count_by_occu[occu] for occu in count_by_occu])
	x_sorted_item=x_item[np.argsort(y_item)]
	y_sorted_item=y_item[np.argsort(y_item)]
		
	pos=np.arange(len(x_sorted_item))
	width=2.0
	
	ax=plt.axes()
	ax.set_xticks(pos+(width/2))
	ax.set_xticklabels(x_sorted_item)
	plt.bar(pos,y_sorted_item,width,color='lightblue')
	plt.show();

#按照用户的年龄情况打印分布图
def print_user_age_dis():
	ages=user_fields.map(lambda fields:int(fields[1])).collect()
	print "##################################################"
	plt.hist(ages,bins=20,color='lightblue',normed=True)
	#below code just nessary by spark-submit
	plt.xlabel('Smarts')
        plt.ylabel('Probability')
	plt.show()
	fig=plt.gcf()
	fig.set_size_inches(16,10)

if __name__=="__main__":
	# print_occuration_info()
	print_user_age_dis()


