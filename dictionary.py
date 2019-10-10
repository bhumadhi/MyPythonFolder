# -*- coding: utf-8 -*-
"""
Created on Mon May  6 17:42:12 2019

@author: bhuwan.madhikarmi
"""

locations = {'North America': {'USA': ['Mountain View']}}

locations['Asia']={'India':['Bangalore']}

locations['North America']['USA'].append('Atlanta')

#locations['Africa']['Egypt'].append('Cairo') # this is not allowed since africa is not there 
locations['Africa']={'Egypt':['Cairo']}

locations['Asia']['China'] = ['Shanghai']

#print(locations)

usa_sorted = sorted(locations['North America']['USA'])
for city in usa_sorted:
    print(city)
    
asia_countries = []
for country, cities in locations['Asia'].iteritems():
    city


5+2
_
a, _,  b = (1,2,3)
print(a,b)

num = 10
#num + 5
num.__add__(5)

class employee:
    def __new__(cls):
        print ("__new__ magic method is called")
        inst = object.__new__(cls)
        return inst
    def __init__(self):
        print ("__init__ magic method is called")
        self.name='Satya'
e1= employee()        

hash(1)
hash(2)
hash('apple')
hash('a')
ord('a')