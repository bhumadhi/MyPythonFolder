# -*- coding: utf-8 -*-
"""
Created on Fri May  3 16:26:33 2019

@author: bhuwan.madhikarmi
"""

def binary_search(input_array, value):
    low = 0
    high = len(input_array) - 1
    while low <= high:
        mid = int((low+high) /2)
        #print(mid)
        if input_array[mid] == value:
            return mid
        elif value < input_array[mid]:
            high = mid-1
        else:
            low = mid+1
    return -1

test_list = [1,3,9,11,15,19,29]
test_val1 = 25
test_val2 = 15
print (binary_search(test_list, test_val1))
print (binary_search(test_list, test_val2))

n=5
print(f"{n}")