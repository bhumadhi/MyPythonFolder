# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 15:02:15 2019

@author: bhuwan.madhikarmi
"""

# importing libaries
import pandas as pd, numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# reading the csv data
student_data = pd.read_csv("C:/Users/bhuwan.madhikarmi/Documents/MyPythonFolder/student-data.csv")

# showing 5 randomly selected samples of the dataset
student_data.sample(5)

#dimensions of data
print("Amount of rows:", len(student_data))
print("Amount of attributes:", len(student_data.columns))

# take a look on the statistic of the numeric variables
student_data.describe()

# displaying all features
student_data.columns

sns.distplot(student_data['age'], kde=False)

sns.distplot(student_data['failures'], kde=False)

frame = pd.DataFrame(index = np.arange(len(student_data['failures'])), columns=("Age","Failed", "Failures"))
for i, row in student_data.iterrows():
    frame.loc[i] = [row['age'], row['failures'] > 0, row['failures']]
    
sns.catplot(y="Age", hue="Failed", kind="count",
        palette="pastel", edgecolor=".6",
        data=frame);
# Separate data into features and target variabbles
columns = list(student_data.columns)
columns.remove("passed")
feature_cols = columns # all columns except passed
target_col = ['passed'] # passed is target column
print("Feature column(s):-\n{}".format(feature_cols))
print("Target column: {}".format(target_col))   

X = student_data[feature_cols]  # feature values for all students
y = student_data[target_col]  # corresponding targets/labels
print("\nFeature values:-")
print(X.sample(5))  # print the 5 samples

# Preprocess feature columns
# encoding of binary and nominal data
def preprocess_features(X):
    # initate empty dataframe, where we saved the transformed data
    outX = pd.DataFrame(index=X.index)  
    # Check each column by iterating through items
    for col, col_data in X.iteritems():
        # If data type is non-numeric, try to replace all yes/no values with 1/0
        # binary case
        if col_data.dtype == object:
            # changing colums to int 
            col_data = col_data.replace(['yes', 'no'], [1, 0])
            
        # If still non-numeric, convert to one or more dummy variables
        # nominal case
        if col_data.dtype == object:
             # e.g. 'guardian' => 'guardian_mother', 'guardian_father', ... 
            col_data = pd.get_dummies(col_data, prefix=col) 
        
        # collect data in output frame
        outX = outX.join(col_data)  

    return outX

X = preprocess_features(X)
print(X.head)
print("Processed feature columns (%s):-\n{%s}" % (str(len(X.columns)), str(list(X.columns))))


# split data into 75% train and 25% test
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42, shuffle=True)


"""testing from udemy
# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_predict)
testing from udemy"""

# Class to store different information about a trained classifier
class ClassifierInfo:
    def __init__(self, clf, training_time, prediction_time, f1_score):
        self.clf = clf
        self.t = training_time
        self.p = prediction_time
        self.f1_score = f1_score

import time

# train a model and measure the time, output of time in seconds
def train_classifier(clf, X_train, y_train):
    print("Training {}...".format(clf.__class__.__name__))
    start = time.time()
    clf.fit(X_train, y_train)
    end = time.time()
    difference = round((end - start),3)
    print("Done!\nTraining time (secs): {:.3f}".format(difference))
    return difference

# predict with a model and measure the time needed for the prediction
# return y_pred for further computations

def predict_classifier(clf, X_test, y_test):
    print("Prediction {}...".format(clf.__class__.__name__))
    start = time.time()
    y_pred = clf.predict(X_test)
    #print(y_pred)
    end = time.time()
    difference = round((end - start),3)
    print("Done!\nPrediction time (secs): {:.3f}".format(difference))
    return difference, y_pred     

import sklearn

# function to measure f1score
def f1score(y_true, y_pred):
    return sklearn.metrics.f1_score(y_true, y_pred, average='weighted') 
from sklearn.metrics import accuracy_score
# coordination function for training, predicting and measuring
def train_predict(clf, X_train, y_train, X_test, y_test):
    print("------------------------------------------")
    print("Training set size: {}".format(len(X_train)))
    training_time = train_classifier(clf, X_train, y_train)
    prediction_time, y_pred = predict_classifier(clf, X_test, y_test)
    #print(y_pred)
    f1_score = f1score(y_test, y_pred )
    print("F1 score of {} is {}".format(clf.__class__.__name__, f1_score))
    print(accuracy_score(y_test, y_pred))
    return ClassifierInfo(clf, training_time, prediction_time, f1_score) , pd.DataFrame(data=y_pred)  

#y_predict.rename(columns = {0:'Pred_passed'}, inplace = True)
#y_predict_knn.rename(columns={'0':'pred_passed'}) #dont do it

from sklearn.naive_bayes import GaussianNB
nb = GaussianNB()
#nb_info, y_predict = train_predict(nb, X_train, y_train, X_test, y_test)
nb_info, y_predict_nb = train_predict(nb, X_train, y_train.values.reshape(-1,), X_test, y_test.values.reshape(-1,))



from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier(n_neighbors=5)
knn_info, y_predict_knn = train_predict(knn, X_train, y_train.values.reshape(-1,), X_test, y_test.values.reshape(-1,))

from sklearn import svm
svc = svm.SVC()
#svm_info, y_predict = train_predict(svc, X_train, y_train, X_test, y_test)
svm_info, y_predict_svc = train_predict(svc, X_train, y_train.values.reshape(-1,), X_test, y_test.values.reshape(-1,))

y_test.rename(columns = {'passed':'org_passed'}, inplace = True)
y_predict_nb.rename(columns = {0:'Pred_passed_nb'}, inplace = True)
y_predict_knn.rename(columns = {0:'Pred_passed_knn'}, inplace = True)
y_predict_svc.rename(columns = {0:'Pred_passed_svc'}, inplace = True)
#y_test
#print(pd.DataFrame(data=y_predict))

#y_test.to_csv("C:/Users/bhuwan.madhikarmi/Documents/MyPythonFolder/y_test.csv", sep='\t')
#y_predict.to_csv("C:/Users/bhuwan.madhikarmi/Documents/MyPythonFolder/y_pred.csv", sep='\t')

#result = pd.merge(y_test,y_predict)

#print("X=%s, Predicted=%s" % (y_test[0], y_predict[0]))


#df = X_test.reset_index(drop=Tru‌​e).merge(y_predict.reset_index(drop=Tru‌​e), left_index=True, right_index=True, how='left')



df_1 = pd.concat([X_test.reset_index(),y_test.reset_index(drop='Tru‌​e')],axis=1)

df_nb = pd.concat([df_1.reset_index(drop='Tru‌​e'),y_predict_nb.reset_index(drop='Tru‌​e')],axis=1)
df_knn = pd.concat([df_1.reset_index(drop='Tru‌​e'),y_predict_knn.reset_index(drop='Tru‌​e')],axis=1)
df_svc = pd.concat([df_1.reset_index(drop='Tru‌​e'),y_predict_svc.reset_index(drop='Tru‌​e')],axis=1)

student_data.to_csv("C:/Users/bhuwan.madhikarmi/Documents/MyPythonFolder/student_data.csv")
df_1.to_csv("C:/Users/bhuwan.madhikarmi/Documents/MyPythonFolder/df_1.csv")
df_nb.to_csv("C:/Users/bhuwan.madhikarmi/Documents/MyPythonFolder/df_nb.csv")
df_knn.to_csv("C:/Users/bhuwan.madhikarmi/Documents/MyPythonFolder/df_knn.csv")
df_svc.to_csv("C:/Users/bhuwan.madhikarmi/Documents/MyPythonFolder/df_svc.csv")





