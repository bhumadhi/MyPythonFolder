# -*- coding: utf-8 -*-
"""
Created on Fri Nov 16 13:16:36 2018

@author: bhuwan.madhikarmi
"""

import pandas as pd
import numpy as np
import operator 

print("---------------------")
print("IMPORT DATASET")
print("---------------------")
dataset = pd.read_csv("C:/Users/bhuwan.madhikarmi/Documents/MyPythonFolder/iris.csv")

print("Dataset Properties:")
print("---------------------")
print("sample dataset rows:")
dataset.head()
print("length of dataset: "+str(len(dataset)))
print("shape of dataset: ")
print(dataset.shape)
nRows = dataset.shape[0]
nCols = dataset.shape[1]
print("number of rows/lines: "+ str(nRows))
print("number of cols/attributes: "+ str(nCols))

"""
print("---------------------------")
print("EUCLIDEAN DISTANCE FUNCTION")
print("--------------------------")
"""
def euclideanDistance(dataPoint1, dataPoint2, length):
    distance = 0
    for i in range(length):
        distance += np.square(dataPoint1[i]-dataPoint2[i])        
    return np.sqrt(distance)
        
"""
print("---------------------------")
print("KNN FUNCTION")
print("--------------------------")
"""
def knn(trainingSet, testInstance, k):

    #calculate euclidean distance of testInstance point to every data point in trainingSet
    distances = {}
    length = testInstance.shape[1]
    for i in range(len(trainingSet)):
        #print("len(trainingSet): "+str(i)+":"+str(len(trainingSet)))
        dist = euclideanDistance(testInstance, trainingSet.iloc[i], length)
        #print("dist: : "+ str(dist))
        distances[i] = dist[0]

    #sort the distances
    sorted_dist = {}
    sorted_dist = sorted(distances.items(), key=operator.itemgetter(1))
    
    #extract top k distances/neighbours
    neighbors = []
    for i in range(k):
        #neighbours[i] = sorted_dist[i]
        neighbors.append(sorted_dist[i][0])
    
    #calculate the most frequent neighbour
    occurence = {}
    for i in range(k):
        response = trainingSet.iloc
    

testInstance =  [[7.2, 3.6, 5.1, 2.5]]  
test = pd.DataFrame(testInstance)
k = 3
print("Value of k chosen = " + str(k))   
knn(dataset, test, k)  





fruit1 = ["b","a","c"]
print(fruit1)
fruit2 = {"b","a","c"}
print(fruit2)
