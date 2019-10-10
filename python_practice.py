# -*- coding: utf-8 -*-
"""
Created on Fri May 17 16:37:34 2019

@author: bhuwan.madhikarmi
"""

#print
print("hello world")
my_string = "hello world"
print(my_string)

#formatted print
n = int(input())
for i in range(1,n+1):
    print(f"{i}", end = " ")
for j in range(1,n+1):    
    print(j, end = ",")

#if-else
if __name__ == "__main__":
    n = int(input())
    if n in range(0,10):
        if n % 2 == 1:
            print("odd")
        elif(n % 2 == 0):
            print("even")
    elif n > 10:
        print("n is greater than 10")
    else:
        print("nothing")
   
#arithmetic operations     
if __name__ ==  "__main__":
    a = int(input())
    b = int(input())
    
    if a in range(1, 10**10+1): # 0 < a <= 10^10
        if b in range (1, 10*10+1): # 0 <b <=10power10
            print(a+b)
            print(a-b)
            print(a//b) # integer division
            print(a/b) # float division(normal)

#list comprehensions
x=[1,2,3,4,5]
y = [x[i] for i in range (len(x))]
print(y)

x=[1,2,3,4,5]
y = [x[i] for i in range (len(x)) if x[i] < 4]
print(y)            

if __name__ == '__main__':
    x, y, z, n = [int(input()) for _ in range(4)] #taking four inputs using loop
    listOfAnswers = [[i, j, k] for i in range(x + 1) for j in range(y + 1) for k in range(z + 1) if i + j + k != n]
    print(listOfAnswers)            

#sum of elements of array
def sum_array(arr)     :
    sum = 0
    for i in range(len(arr)):
        sum = sum + arr[i]
    return sum

def main():
    arr_length = int(input())
    print("arr_length: " + str(arr_length))
    #arr2 = [[int(input())] for _ in range(arr_length)]
    
    #this is one way to take inputs and put them in a list
    arr2 = [int(input().strip()) for _ in range(arr_length)]
    
    #this is another way to take inputs and put them in a list
    arr3 = list(map(int,input().rstrip().split()))
    print(arr2)
    print("sum of arr2")
    print(sum_array(arr2))
    print(arr3)
    print("sum of arr3")
    print(sum_array(arr3))    
    
if __name__ == "__main__":
    main()
    

ex = "10 20 30 40 "
print(ex.rstrip()) 
print(ex.rstrip().split())  
print(map(int,ex.rstrip().split()))
print(list(map(int,ex.rstrip().split())) )
  
inputs = "  10 20 30 40  "
print(list(map(int,inputs.strip().split())))
  
inputs = "         10 20 30 40     "
print(inputs.lstrip())
print(inputs.rstrip())
print(list(map(int,inputs.lstrip().split())))

print(list(map(int,input().strip().split())))
print(list(map(int,input().rstrip.split())))


n = int(input())
arr = [[1,2,3],[4,5,6],[7,8,9]]
#for _ in range(n):
#    arr.append(list(map(int,input().strip().split())))
print(arr)    
left_diag_arr = [arr[i][i] for i in range(n)]
print(left_diag_arr)
right_diag_arr = [arr[i][j] for i in range(n) for j in range(n-1,0,-1)]
print(right_diag_arr)

    

tes_arr = [[1,2,3],[4,5,6],[7,8,9]]
n = len(tes_arr)
right_arr=[]
#print([tes_arr[i][j] for i in range(0,len(tes_arr),1) for j in range(len(tes_arr)-1,0,-1)])
for i in range(0,n,1):
        print("i:"+str(i)+ " j:"+str(i))
        print(tes_arr[i][i])        
        print("i:"+str(n-1-i)+ " j:"+str(i))        
        print(tes_arr[n-1-i][i])
#        right_arr.append(tes_arr[i][j])
print(right_arr)    

n=2
sum1=0
sum2=0
a = [[1,2],[5,9]]
for i in range(n):
    sum1 += a[i][i];
    sum2 += a[n-i-1][i];  
print(sum1)    
print(sum2)    


#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the diagonalDifference function below.
def diagonalDifference(arr):
    diag_left = 0
    diag_right = 0
    for i in range(len(arr)):
        diag_left += arr[i][i]
        diag_right += arr[n-1-i][i]
    return abs(diag_left-diag_right)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))
        #or
#    n = int(input()) 
#    a = []
#    for i in range(n):
#        a.append([int(j) for j in input().split()])

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
    
    
def plusMinus(arr):
    cplus=0
    cminus=0
    czero=0    
#    for i in range(len(arr)):
#        if arr[i]>=-100 and arr[i]<=100:
#            if arr[i]>0:
#                cplus +=1
#            elif arr[i] == 0:
#                czero +=1
#            else:
#                cminus +=1
#        else:
#            return -1
    for elem in arr:
        if elem>=-100 and elem<=100:
            if elem>0:
                cplus +=1
            elif elem == 0:
                czero +=1
            else:
                cminus +=1
        else:
            return -1        
#    print("positive:")
    if cplus == 0:
        print(0)
    else:
        print(round(cplus/len(arr),6))
#    print("negative:")        
    if cminus == 0:
        print(0)
    else:
        print(round(cminus/len(arr),6))        
#    print("zero:")        
    if czero == 0:
        print(0)
    else:
        print(round(czero/len(arr),6))        
                      
if __name__ == '__main__':
    n = int(input())
    if n in range(0,101):
        arr = list(map(int, input().rstrip().split()))    
plusMinus(arr)        
    
    
    
    
    
