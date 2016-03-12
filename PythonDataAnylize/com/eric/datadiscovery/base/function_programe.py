# -*- coding: utf-8 -*-
'''主要演示如何使用函数式的语法'''
__author__ = 'Eric'
from functools import reduce

#定义map的操作函数
multi_fun=lambda x:x*2

#定义reduce的操作函数，该函数需要两个参数
reduce_fun=lambda x,y:x+y
#定义操作结合
item_list=[i*1 for i in range(10)]

#使用multi_fun对item_list的元素进行逐个的处理
def map_sample():
    map_result=map(multi_fun,item_list)
    #返回map对象，需要使用list函数进行转换
    list_object=list(map_result)
    print(list_object)

#使用reduce_fun对item_list的元素进行递归处理，例如item_list包含10个元素，reduce会首先使用第一个，第二个元素带入reduce_fun中进行处理，
# 处理的结果和第三个元素作为参数再次带入到reduce_fun中进行处理，直到处理完所有的元素，得到一个结果
def reduce_sample():
    result=reduce(reduce_fun,item_list)
    print(result)

#filter使用函数来对元素列表进行过滤
def filter_sample():
    #只输出偶数
    result=list(filter(lambda x: x%2==0,item_list))
    print(result)

#使用map,reduce,filter相比于for,while除了语法比较简单外，效率也比较高。下面的例子用来对比reduce和for的效率对比
def compare_effective():
    loop_times=10000000
    import time
    reduce_start_time=time.time()
    reduce_result=reduce(reduce_fun,range(loop_times))
    reduce_end_time=time.time()


    for_start_time=time.time()
    for_result=0
    for i in range(loop_times):
        for_result+=i;
    for_end_time=time.time()

    print("reduce 运行时间:"+str(reduce_end_time-reduce_start_time)+" 结果是："+str(reduce_result))
    print("for 运行时间:"+str(for_end_time-for_start_time)+" 结果是："+str(for_result))


#map_sample()
#reduce_sample()
#filter_sample()
compare_effective()