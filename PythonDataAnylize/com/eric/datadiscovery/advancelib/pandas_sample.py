# -*- coding: utf-8 -*-
from pandas import Series,DataFrame
import pandas as pd

s=Series([1,2,3],index=['a','b','c'])
d=DataFrame([[1,2,3],[4,5,6]],columns=['a','b','c'])

#head() method will return top 5 records
print s.head()
print s.describe()
print d.head()
print d.describe()

#read data from xml file
excel_data=pd.read_excel("./server.xlsx")
print excel_data.head