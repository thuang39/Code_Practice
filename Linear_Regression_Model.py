from pandas import read_csv
import pandas as pd
import numpy as np
import math
import sys

x = pd.read_csv('training_data.csv', header = None)
y = pd.read_csv('training_labels.csv', header = None)
xhat = pd.read_csv('testing_data.csv', header = None)
ylabel = pd.read_csv('testing_labels.csv', header = None)
#print x

#step 1
x = np.array(x)
y = np.array(y)

#step 2
x = np.c_[ np.ones(1000), x ]
#print x
#print('\n')
#print x.transpose()
#print y

#step 3
w = np.dot(np.dot(np.linalg.inv(np.dot(x.transpose(), x)), x.transpose()), y)
#print w

#step 4
xhat = np.array(xhat)
xhat = np.c_[ np.ones(1000), xhat ]
ylabel = np.array(ylabel)
yhat = np.dot(xhat, w)
#print yhat
#print('\n')
#print ylabel
#print('\n')
print math.sqrt(np.sum(np.power(np.subtract(yhat, ylabel), 2))/1000)