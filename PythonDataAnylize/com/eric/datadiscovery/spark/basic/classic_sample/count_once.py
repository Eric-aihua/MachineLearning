# -*- encoding:utf-8-*-
'''原始数组中所有的元素理论上都应该出现偶数次，该程序可以方便的找到出现奇数次的数，解决问题的思路如下：
   1，对RDD中每个分区的数据进行异或操作
   2，对步骤1的结果再次进行异或操作
   3，当一个数字进行偶数次异或时，结果等于0，否则等于该数本身，由此得到出现奇数次的那个数
'''
from pyspark import SparkContext
from functools import reduce
sc = SparkContext(appName='mid_number')
base_array=range(10000000)*4
base_array.append(1883)
odd_rdd=sc.parallelize(base_array)
#异或函数
odd_func=lambda x,y:x^y
#对每个分区进行处理的函数
def odd(chain):
	result=reduce(odd_func,chain)
	yield (1,result)
par_rdd=odd_rdd.mapPartitions(odd).cache()
par_result=par_rdd.collect()
#对每个分区的结果再次进行异或操作，最后的结果就是奇数次出现的那个数
final_result=par_rdd.reduceByKey(lambda x,y:x^y).collect()[0][1]
print par_result
print final_result


		

