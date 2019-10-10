# -*- coding: utf-8 -*-
"""
Created on Thu Dec 13 14:32:25 2018

@author: bhuwan.madhikarmi
"""

data = pd.read_csv("C:/Users/bhuwan.madhikarmi/Desktop/data.csv",header = None)
#print (data[0][0]);
print("Number of Rows:",len(data))
#print("Data imported using pandas:",data);
print(data.iloc[5:7,2:3]);
print(data.iloc[5:7]);
print(data.iloc[5:7,:]);
print(data.shape)
print(data.shape[0])
print(data.shape[1])


#http://www.datasciencemadesimple.com/get-maximum-value-column-python-pandas/
#Create Dataframe:
import pandas as pd
import numpy as np
 
#Create a DataFrame
d = {
'Name':['Alisa','Bobby','jodha','jack','raghu','Cathrine',
'Alisa','Bobby','kumar','Alisa','Alex','Cathrine'],
'Age':[26,24,23,22,23,24,26,24,22,23,24,24],
 
'Score':[85,63,55,74,31,77,85,63,42,62,89,77]}
 
df = pd.DataFrame(d,columns=['Name','Age','Score'])
df
# get the maximum values of all the column in dataframe
 
df.max()
# get the maximum value of the column 'Age'
 
df['Age'].max()
# get the maximum value of the column 'Name'
 
df['Name'].max()
This gives the maximum va