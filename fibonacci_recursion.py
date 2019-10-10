# -*- coding: utf-8 -*-
"""
Created on Mon May  6 14:59:12 2019

@author: bhuwan.madhikarmi
"""
#using recursion is slower
def fib(n):
    if n==0 :
        return 0
    elif n==1:
        return 1
    else:
        return fib(n-1)+fib(n-2)
print(fib(5))

#using loop is faster
def fibi(n):
    a, b = 0, 1
    for i in range(n):
        print(str(i)+"a:"+str(a))
        a, b = b, a + b
    return a
print(fibi(9))

def fibin(n):
    a = 0
    b = 1
    for i in range(n):
        t = a
        a = b
        b = t+b
        print(str(i)+"a:"+str(a))        
    return a
print(fibin(9))

def fibin(n):
    a = 0
    b = 1
    for i in range(n):
        c = a+b
        a = b
        b = c
    return a
print(fibin(9))

def get_fib(position):
    if position == 0:
        return 0
    elif position == 1:
        return 1
    else:
        return get_fib(position-1)+get_fib(position-2)

# Test cases
print (get_fib(9))
print( get_fib(11))
print( get_fib(0))