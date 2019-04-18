# Multiple Linear Regression

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('busrouteedit.csv')
X = dataset.iloc[:, 2:-1].values
y = dataset.iloc[:, -1].values


#Xtopred = pd.read_csv('topred.csv')
#Xtp = Xtopred.iloc[:, 2:].values
#dfXtp = pd.DataFrame(Xtp)

# Encoding categorical data
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
labelencoder = LabelEncoder()
X[:, 0] = labelencoder.fit_transform(X[:, 0])
X[:, 1] = labelencoder.fit_transform(X[:, 1])

#Xtp[:, 0] = labelencoder.fit_transform(Xtp[:, 0])
#Xtp[:, 1] = labelencoder.fit_transform(Xtp[:, 1])

onehotencoder = OneHotEncoder(categorical_features = [1])
X = onehotencoder.fit_transform(X).toarray()

#Xtp = onehotencoder.fit_transform(Xtp).toarray()

# Avoiding the Dummy Variable Trap
X = X[:, 1:]



X_final = X[:360, :]
y_final = y[:360]


# Splitting the dataset into the Training set and Test set
from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X_final, y_final, test_size = 1/6, random_state = 0)

# Feature Scaling
"""from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)
sc_y = StandardScaler()
y_train = sc_y.fit_transform(y_train)"""

# Fitting Multiple Linear Regression to the Training set
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, y_train)

# Predicting the Test set results
y_pred = regressor.predict(X_test)
#nowpred = regressor.predict(Xtp)


dfx = pd.DataFrame(X)

X2pred = X[361:, :]
ypreded = regressor.predict(X2pred)


plt.scatter(X_train, y_train, color = 'red')
plt.plot(X_train, regressor.predict(X_train), 'blue')
plt.title("Salary vs Years of Experience")
plt.xlabel("Years of Experience")
plt.ylabel("Salary")
plt.show()

