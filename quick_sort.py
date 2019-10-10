# -*- coding: utf-8 -*-
"""
Created on Mon May  6 16:39:00 2019

@author: bhuwan.madhikarmi
"""

def quick_sort(array):
    #define 3 arrays
    less = []
    equal = []
    greater = []
    
    if len(array)>1:
        #choose a pivot
        pivot = array[0]
        #go through every element and place it in appropriate arrays
        for x in array:
            if x < pivot:
                less.append(x)
            if x == pivot:
                equal.append(x)
            if x > pivot:
                greater.append(x)
        
        return quick_sort(less)+equal+quick_sort(greater)
    else:
        return array
    
quick_sort([6,4,4,4,7,1,2,9,12,3])