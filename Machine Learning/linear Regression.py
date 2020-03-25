import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LinearRegression

# Importing the datasets
 
datasets = pd.read_csv('data/Salary_Data.csv')
X = datasets.iloc[:, :-1].values
Y = datasets.iloc[:, 1].values

# Splitting the dataset into the Training set and Test set

from sklearn.model_selection import train_test_split
X_Train, X_Test, Y_Train, Y_Test = train_test_split(X, Y, test_size = 0.33, random_state = 32)

# Fitting Simple Linear Regression to the training set

regressor = LinearRegression()
regressor.fit(X_Train, Y_Train)

# Predicting the Test set result ￼

Y_Pred = regressor.predict(X_Test)


# Visualising the Training set results
plt.scatter(X_Train, Y_Train, color = 'green')

# Visualising the Testing set results
plt.scatter(X_Test, Y_Test, color = 'red')

# Visualising the regression line
plt.plot(X_Train, regressor.predict(X_Train), color = 'blue')
plt.title('Salary vs Experience')
plt.xlabel('Years of experience')
plt.ylabel('Salary')
plt.show()
