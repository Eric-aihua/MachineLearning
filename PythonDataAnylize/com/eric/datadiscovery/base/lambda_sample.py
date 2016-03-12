# -*- coding: utf-8 -*-
'''主要演示如何使用lambda'''
__author__ = 'Eric'

add_func=lambda x,y:x+y
mul_func=lambda x,y:x*y
sub_func=lambda x,y:x-y
dev_func=lambda x,y:x/y

def cal(fun,x,y):
    result=fun(x,y)
    print( "结果："+str(result))

#将各个操作作为参数传到cal方法，进行执行。
cal(add_func,10,5)
cal(mul_func,10,5)
cal(sub_func,10,5)
cal(dev_func,10,5)

