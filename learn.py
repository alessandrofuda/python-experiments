import pandas as pd
import matplotlib.pyplot as plt

# defining dataframe
df = pd.read_csv('salaries.csv')
df.head()
# x = df.iloc[:,:]
# x = df.iloc[:,:-1].values  # array return
# x = df.iloc[:,-1].values
x = df.iloc[:,:-1].values  # ':-1' IMPORTANT!
# print(x)
# print(x[0:5])

y = df.iloc[:,-1].values   # '-1' IMPORTANT!

# visual representation of linear regression
# plt.scatter(x, y)
# plt.show()


# SPLIT all DATA into: Training and Testing data
# import only a function directly from a submodule of sklearn module (alternative syntax) - (only for memory optimization)
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=0)
# x_train.shape
# x_test.shape
# y_train.shape
# y_test.shape

# Model in action: Build, Train, Predict, Evaluate
from sklearn.linear_model import LinearRegression
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

plt.scatter(x_test, y_test)
plt.plot(x_test, y_pred, color='yellow')
plt.show()
