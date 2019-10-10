# -*- coding: utf-8 -*-
"""
Created on Mon Dec 10 09:43:22 2018

@author: bhuwan.madhikarmi
"""

from random import shuffle;
from random import uniform;
import sys;
import math;
import numpy as np;

#STEP 1
#Read the txt file and load into a list
def ReadData(fileName):
    f = open(fileName, 'r');
    lines = f.read().splitlines();
    #print("lines:",len(lines))
    f.close();
    items = [];
    for i in range (1,len(lines))    :
        line = lines[i].split(',');
        itemFeatures = [];
        
        for j in range (len(line)-1):
            itemFeatures.append(float(line[j]));
        
        items.append(itemFeatures);

    shuffle(items);
    return items;

#STEP 2
#Initialize Means
    
#Find minimum and maximum values of all the features(here 4 columns)
#The variables minima, maxima are lists containing the min and max values of the items respectively. 
def FindColMinMax(items): 
    n = len(items[0]); 
    #print("n:",n);
    minima = [sys.maxsize for i in range(n)]; 
    maxima = [-sys.maxsize -1 for i in range(n)]; 
    #print("initial minima:",minima);
    #print("initial maxima:",maxima);    
    #print("len(items):",len(items))
    for item in items: 
        #print("len(item):",len(item))
        for f in range(len(item)): 
            if (item[f] < minima[f]): 
                minima[f] = item[f]; 

            if (item[f] > maxima[f]): 
                maxima[f] = item[f]; 
    #print("final minima:",minima);
    #print("final maxima:",maxima);

    return minima,maxima; 


def InitializeMeans(items, k, cMin, cMax): 
  
    # Initialize means to random numbers between 
    # the min and max of each column/feature     
    f = len(items[0]); # number of features 
    print("Number of features:",f);
    print("Number of clusters:",k);
    print("cMin:",cMin);
    print("cMax:",cMax);
    means = [[0 for i in range(f)] for j in range(k)]; 
    print("Initialize Means with 0 :",means);
    counter = 0;
    for mean in means: #iterate 3 times = number of cluster
        #print("counter",counter);
        counter +=1;
        for i in range(len(mean)): #iterate 4 times = number of features 
            #print("len(mean):",len(mean));
            # Set value to a random float between minimum and maximum values
            # (adding +-1 to avoid a wide placement of a mean) 
            mean[i] = uniform(cMin[i]+1, cMax[i]-1); 
            #print("cMin[",i,"]:",cMin[i]);
            #print("cMax[",i,"]:",cMax[i]);
            #print(" mean[",i,"]:", mean[i]);
    print("Random values in Means",means);
    return means; 
# Defining a function which calculates euclidean distance between two data points
#here "length" is the number of cloumns in the testInstance, so it is 4 not 5
#iterator runs from 0 to 3
def euclideanDistance(data1, data2, length):
    distance = 0
    
    for x in range(length):
        #print("inner iteration: ",x,": ",np.sqrt(np.square(data1[x] - data2[x])))
        distance += np.square(data1[x] - data2[x])
        #"distance" variable holds sum of distances of each feature between the test instance and ecah of the training instances
        #calculate the distance between each feature and sum them up
        #print("x=",x," data1=",(data1[x]))
    return np.sqrt(distance)

#this is another using math instead of numpy
def EuclideanDistance(x, y): 
    S = 0; #  The sum of the squared differences of the elements 
    for i in range(len(x)): 
        S += math.pow(x[i]-y[i], 2); 
  
    return math.sqrt(S); #The square root of the sum 


def UpdateMean(n,mean,item): 
    for i in range(len(mean)): 
        m = mean[i]; 
        m = (m*(n-1)+item[i])/float(n); 
        mean[i] = round(m, 3); 
      
    return mean;
def FindClusters(means,items):
    clusters = [[] for i in range(len(means))]; #Init clusters
    
    for item in items:
        #Classify item into a cluster
        index = Classify(means,item);

        #Add item to cluster
        clusters[index].append(item);

    return clusters;

def Classify(means,item): 
  
    # Classify item to the mean with minimum distance     
    minimum = sys.maxsize; 
    index = -1; 
  
    for i in range(len(means)): 
  
        # Find distance from item to mean 
        dis = EuclideanDistance(item, means[i]); 
  
        if (dis < minimum): 
            minimum = dis; 
            index = i; 
      
    return index; 


def CalculateMeans(k,items,maxIterations=100000): 
  
    # Find the minima and maxima for columns 
    cMin, cMax = FindColMinMax(items); 
      
    # Initialize means at random points 
    means = InitializeMeans(items,k,cMin,cMax); 
      
    # Initialize clusters, the array to hold 
    # the number of items in a class 
    clusterSizes= [0 for i in range(len(means))]; 
  
    # An array to hold the cluster an item is in 
    belongsTo = [0 for i in range(len(items))]; 
  
    # Calculate means 
    for e in range(maxIterations): 
  
        # If no change of cluster occurs, halt 
        noChange = True; 
        for i in range(len(items)): 
  
            item = items[i]; 
  
            # Classify item into a cluster and update the 
            # corresponding means.         
            index = Classify(means,item); 
  
            clusterSizes[index] += 1; 
            cSize = clusterSizes[index]; 
            means[index] = UpdateMean(cSize,means[index],item); 
  
            # Item changed cluster 
            if(index != belongsTo[i]): 
                noChange = False; 
  
            belongsTo[i] = index; 
  
        # Nothing changed, return 
        if (noChange): 
            break; 
  
    return means;
###_Main_###
def main():
    items = ReadData('C:/Users/bhuwan.madhikarmi/Desktop/data.txt');
    
    k = 3;

    means = CalculateMeans(k,items);
    clusters = FindClusters(means,items);
    print ("Final Means",means);
    print ("clusters",clusters);

    #newItem = [5.4,3.7,1.5,0.2];
    #print Classify(means,newItem);

if __name__ == "__main__":
    main();

"""
def FindMin(items): 
    n = len(items[0]); 
    minima = [sys.maxsize for i in range(n)]; 
    for item in items: 
        #print("len(item):",len(item))
        for f in range(len(item)): 
            if (item[f] < minima[f]): 
                minima[f] = item[f]; 
    #print("final minima:",minima);
    return minima; 

def FindMax(items): 
    n = len(items[0]); 
    maxima = [-sys.maxsize -1 for i in range(n)]; 
    for item in items: 
        #print("len(item):",len(item))
        for f in range(len(item)): 
            if (item[f] > maxima[f]): 
                maxima[f] = item[f]; 
    #print("final maxima:",maxima);                
    return maxima; 
"""
"""FindColMinMax(
ReadData('C:/Users/bhuwan.madhikarmi/Desktop/data.txt')
);
"""
"""

InitializeMeans(
    ReadData('C:/Users/bhuwan.madhikarmi/Desktop/data.txt'),
    3,
    FindMin(
            ReadData('C:/Users/bhuwan.madhikarmi/Desktop/data.txt')
            ),
    FindMax(
            ReadData('C:/Users/bhuwan.madhikarmi/Desktop/data.txt')
            )    
        );
"""    
    