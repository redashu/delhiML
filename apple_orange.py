#!/usr/bin/python3

from sklearn import tree
#  to make a diffence we need to create a dataset
#        weight , texture
#  smooth means 0 and bumpy  means 1
features=[[100,0],[120,0],[130,1],[140,1]]
# label 
output=["apple","apple","orange","orange"]

# making decision tree classifier

algo=tree.DecisionTreeClassifier()
trained=algo.fit(features,output)

# now time for predicting  the fruits 
fruit=trained.predict([[129,0]])

# print the output
print(fruit)
###########



