'''python program for k-nearest neighbour using scikit-learn'''
from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier #classifier function from sklearn
import numpy as np
import random


#to split the data set into training and testing set
from sklearn.model_selection import train_test_split

#available dataset in scikit library
iris_dataset=load_iris()

X_train, X_test, y_train, y_test = train_test_split(iris_dataset["data"], iris_dataset["target"], random_state=0)

#value of k=1 here
kn = KNeighborsClassifier(n_neighbors=1)

#training the model
kn.fit(X_train, y_train)

index = random.randrange(0,len(X_test)+1)

#testing of trained model
prediction = kn.predict([X_test[index]])

print("Predicted target value: {}\n".format(prediction))
print("Predicted feature name: {}\n".format(iris_dataset["target_names"][prediction]))