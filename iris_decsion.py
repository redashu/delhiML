#!/usr/bin/python3

from sklearn.datasets import  load_iris  #  loading iris data set
import  numpy as np
from sklearn import  tree  #  loading  decisition tree algo
# load the data
iris=load_iris()

#  random gate generator
sample=[0,50,100]
#  features  are 
x=iris.data
#  lable which means output
y=iris.target

# only picking 49 sample for data training rest one for predict
train_data=np.delete(x,sample)
test_data=iris.data[sample]
# lets work for label
train_target=np.delete(iris.target,sample)

#  calling  decision tree 
algo=tree.DecisionTreeClassifier()
#  training  algo
trained=algo.fit(x,y)
# now to time for arrag 
out=trained.predict(test_data)
print(out)

