# -*- coding: utf-8 -*-
"""
Created on Fri May 17 15:01:41 2019

@author: bhuwan.madhikarmi
"""



random_string = '     this is good'

# Leading whitepsace are removed
print(random_string)
print(random_string.rstrip( ))
print(random_string.rstrip('god s'))

# Argument doesn't contain 'd'
# No characters are removed.
print(random_string.rstrip('si oo'))

print(random_string.rstrip('is good'))

website = 'www.programiz.com/'
print(website.rstrip('m/.'))
        

x = int(input())
y = int(input())
z = int(input())
n = int(input())
list_elem   = []
for i in range(x +1):
    for j in range(y + 1):
        for k in range(z + 1):
            if (i + j + k) != n:
                elem        = []
                elem.insert(0,i)
                elem.insert(1,j)
                elem.insert(2,k)
                list_elem.append(elem)              
print(list_elem)

x, y, z, n = [int(input()) for _ in range(4)]
listOfAnswers = [[i, j, k] for i in range(x + 1) for j in range(y + 1) for k in range(z + 1) if i + j + k != n]
print(listOfAnswers)

x = [1.5,2,3,4]
y = [i for i in x if i<3]
print(y)

x=[1,2,3,4,5]
y = [x[i] for i in range (len(x)) if i < 4]
print(y)

x=[1,2,3,4,5]
y = [x[i] for i in range (len(x)) if x[i] < 4]
print(y)