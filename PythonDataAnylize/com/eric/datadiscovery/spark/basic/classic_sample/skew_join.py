# -*- encoding:utf-8-*-
'''在系统运行过程中，很多时候会由于key分布不均匀，业务数据分布不均匀导致在进行RDD操作的时候出现数据倾斜的情况'''
from pyspark import SparkContext
import random
sc = SparkContext(appName='skew_join')
#存在数据倾斜的列表
skew_list=[('a',random.randint(1,1000)) for i in range(1000000)]
skew_list.append(('b',10))
skew_list.append(('c',8))
#正常的数据列表
normal_list=[('a',9),('b',3),('c',8)]

skew_rdd=sc.parallelize(skew_list)
normal_rdd=sc.parallelize(normal_list)
#skew_rdd.cache()

#如果不进行倾斜处理，则执行join时，会存在处理a的那个task会很慢,单机执行时，最慢的task的时间为2分钟
#××××××××××单机模式下

#print skew_rdd.join(normal_rdd).count()

#进行倾斜处理
#1,先对skew_rdd进行采样，假设只有一个key倾斜，获取倾斜率最大的key
skew_sample=skew_rdd.sample(False,0.3,9).groupByKey()
skew_sample.cache()
skew_sample_count_map=skew_sample.map(lambda (k,v):(len(v),k))
skew_sample_count_map.cache()
max_count=skew_sample_count_map.reduce(lambda x,y:max(x[0],y[0]))[0]
max_count_key=skew_sample_count_map.filter(lambda x:x[0]==max_count).collect()[0][1]

#2，根据步骤1得到的max_count_key,将skew_rdd进行拆分，一部分只包括max_count_key，另外一部分不包括max_count_key,然后分别与normal_rdd进行join,最后将结果union


max_key_rdd=skew_rdd.filter(lambda x:x[0]==max_count_key)
other_key_rdd=skew_rdd.filter(lambda x:x[0]!=max_count_key)
result1=max_key_rdd.join(normal_rdd) 
result2=other_key_rdd.join(normal_rdd) 
print result1.union(result2).count()

