# -*- encoding:utf-8-*-
from pyspark import SparkContext
import random

__author__ = 'eric.sun'

# /**
#  * 求中位数，数据是分布式存储的
#  * 将整体的数据分为K个桶，统计每个桶内的数据量，然后统计整个数据量
#  * 根据桶的数量和总的数据量，可以判断数据落在哪个桶里，以及中位数的偏移量
#  * 取出这个中位数
#  */

sc = SparkContext(appName='mid_number')
array=[random.randint(1,1000) for i in range(1000)]
orgainary_array=sc.parallelize(array)
#对原始数据进行排序
sorted_array=orgainary_array.sortBy(lambda a:a)
#对排序数组进行分组,分组的数量和数据量相关
group_element=sorted_array.map(lambda e:(e/10,e)).sortByKey()
#统计每个分组的元素个数
group_element_count=sorted_array.map(lambda e:(e/10,1)).reduceByKey(lambda x,y:x+y).sortByKey()
group_element_count_map=group_element_count.collectAsMap()
#算出总的元素个数
element_count=group_element_count.map(lambda (k,v):v).sum()



temp=0
index=0
mid=0
temp2=0
if element_count%2!=0:
    mid=element_count/2+1
else:
    mid=element_count/2

pcount=group_element_count.count()
for i in range(pcount):
    temp+=group_element_count_map[i]
    temp2=temp-group_element_count_map[i]
    if temp>=mid:
        #得到中位的index
        index=i
        break

offset=mid-temp2
result=group_element.filter(lambda (k,v):k==index).takeOrdered(offset)
la=list(array)
la.sort()
# print la
print "midnum:%s",result[offset-1][1]





