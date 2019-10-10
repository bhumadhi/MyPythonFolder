# -*- coding: utf-8 -*-
"""
Created on Wed Dec 12 15:16:54 2018

@author: bhuwan.madhikarmi

Reference 
https://mubaris.com/posts/kmeans-clustering/
https://github.com/mubaris/friendly-fortnight
"""
from matplotlib import pyplot as plt
from copy import deepcopy
import numpy as np
import pandas as pd
plt.rcParams['figure.figsize'] = (16,9)
plt.style.use('ggplot')

#Importing the dataset
data = pd.read_csv('C:/Users/bhuwan.madhikarmi/Documents/MyPythonFolder/xclara.csv')
print (data.shape)
data.head()

#Getting the values and plotting it
f1 = data['V1'].values
f2 = data['V2'].values
print(f1)
print(f2)
#f1 = data.iloc[:,0]
#f2 = data.iloc[:,1]
#print(f1)
#print(f2)
X = np.array(list(zip(f1,f2)))
#print(X)
plt.scatter(f1, f2, c='black', s=7)

#def euclideanDistance(data1, data2, length):
#    distance = 0
#    
#    for x in range(length):
#        #print("inner iteration: ",x,": ",np.sqrt(np.square(data1[x] - data2[x])))
#        distance += np.square(data1[x] - data2[x])
#        #"distance" variable holds sum of distances of each feature between the test instance and ecah of the training instances
#        #calculate the distance between each feature and sum them up
#        #print("x=",x," data1=",(data1[x]))
#    return np.sqrt(distance)

# Euclidean Distance Caculator
def dist(a, b, ax=1):
    return np.linalg.norm(a - b, axis=ax)
dist()

# from scipy.spatial import distance
# distance.euclidean([1, 0, 0], [0, 1, 0])

# Number of clusters
k = 3
# X coordinates of random centroids
#C_x = np.random.randint(0, np.max(X)-20, size=k)
C_x = np.random.randint(np.min(X)+20, np.max(X)-20, size=k)
# Y coordinates of random centroids
#C_y = np.random.randint(0, np.max(X)-20, size=k)
C_y = np.random.randint(np.min(X)+20, np.max(X)-20, size=k)
C = np.array(list(zip(C_x, C_y)), dtype=np.float32)
print("Initial Centroids")
print(C)

# Plotting along with the Centroids
plt.scatter(f1, f2, c='#050505', s=7)
plt.scatter(C_x, C_y, marker='*', s=200, c='r')

#











