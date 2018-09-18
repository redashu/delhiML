#!/usr/bin/python3

from sklearn.datasets  import load_iris

from sklearn.model_selection  import  train_test_split
#from sklearn.cross_validation  import  train_test_split
from sklearn  import tree
iris=load_iris()

# divide into training and testing data
# 10%  for  testing  remaining  90%  for training 
train_data,test_data,train_target,test_target=train_test_split(iris.data,iris.target,test_size=0.01)

# calling  decision tree
clf=tree.DecisionTreeClassifier()
#  calling trained algo
trained=clf.fit(train_data,train_target)

#  predict  
output=trained.predict(test_data)
print('predicted output is :  ',output)

########
print('actual output is :   ',test_target)

#  accuracy score
from sklearn.metrics import  accuracy_score 
check=accuracy_score(test_target,output)
print(check)
