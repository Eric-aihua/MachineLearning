# -*- coding: utf-8 -*-
from pyspark import SparkContext

logFile = "/opt/talas/ml-100k/u.user"  # Should be some file on your system
sc = SparkContext("local", "User Statics")
#Data Sample:1|24|M|technician|8571
user_data = sc.textFile(logFile).cache()

#打印出基本的数据情况
user_fields=user_data.map(lambda line:line.split("|"));
user_fields.cache()
num_users=user_fields.map(lambda fields:fields[0]).count()
num_age=user_fields.map(lambda fields:fields[1]).distinct().count()
num_gender=user_fields.map(lambda fields:fields[2]).distinct().count()
num_occupation=user_fields.map(lambda fields:fields[3]).distinct().count()
num_zipcode=user_fields.map(lambda fields:fields[4]).distinct().count()
print "Users: %d  Ages: %d Genders: %d Occupations: %d ZipCodes: %d" % (num_users,num_age,num_gender,num_occupation,num_zipcode)



#使用常规方法统计每个职业的人数
count_by_occu=user_fields.map(lambda fields:(fields[3],1)).reduceByKey(lambda x,y:x+y).collect();
#使用countByValue方法统计每个职业的人数
count_by_occu2=user_fields.map(lambda fields:fields[3]).countByValue()
print count_by_occu