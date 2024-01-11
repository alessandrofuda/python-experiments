# How to predict values via Linear Regression: High-level Logical Process
# 0) split data in 'test' and 'train'
# 1) with 'train' data --> train the model
# 2) with 'test' data --> test/evaluate the model
# 2.a - get test data,
# 2.b - run model through these test data
# 2.c - generate "predicted by trained model" data
# 3) compare 'predicted data' with 'real test' data and calculate percentage of model reliability

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split  # import function directly from submodule of sklearn module
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

# defining/modelling dataframe
df = pd.read_csv('data/salaries.csv')
df.head()
# x = df.iloc[:,:]  # rows,cols --> result contains also 'index' col
# x = df.iloc[:,:-1].values  # array return
# x = df.iloc[:,-1].values
x = df.iloc[:, :-1].values  # ':-1' IMPORTANT!
# x = df.drop(['salary'], axis=1)  # drop column from dataframe, axis=1 is column, axis=0 is index column
# print(x)
# exit()
# print(x[0:5])

y = df.iloc[:, -1].values   # '-1' IMPORTANT!

# visual representation of linear regression
plt.scatter(x, y)
# plt.show()


# SPLIT all DATA into: Training and Testing data
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=0)
# x_train.shape
# y_train.shape

# Model in action: Build, Train, Predict, Evaluate
model = LinearRegression()
model.fit(x_train, y_train)

print('To predict values: 7, 3, 3.5 ')
print('Predicted values: ', end=" ")
print(model.predict([[7], [3], [3.5]]))

print('--------------')

print('x_test: ')
print(x_test)
y_pred = model.predict(x_test)

print('y_pred (predicted): ', end="")
print(y_pred)

# show errors comparing generated-by-model y with real y
error = y_pred - y_test
print('Error: ', end=" ")
print(error)


plt.scatter(x_test, y_test)
plt.plot(x_test, y_pred, color='yellow')
# plt.show()

# calculate model accuracy
r2 = r2_score(y_test, y_pred)
print('Model accuracy: ', end="")
print(r2)
