import pandas as pd
import matplotlib.pyplot as plt

# defining dataframe
df = pd.read_csv('salaries.csv')
df.head()
# x = df.iloc[:,:]
# x = df.iloc[:,:-1].values  # array return
# x = df.iloc[:,-1].values
x = df.iloc[:,0].values
# print(x)
# print(x[0:5])

y = df.iloc[:,1].values

# visual representation of linear regression
plt.scatter(x, y)
# plt.show()


# SPLIT all DATA into: Training and Testing data
# import only a function directly from a submodule of sklearn module (alternative syntax) - (only for memory optimization)
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=0)
x_test.shape
# print(x_train)
# print(x_train.shape)
# print(x_test)
# print(x_test.shape)


# Model in action: Build, Train, Predict, Evaluate
from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(x_train, y_train)
#print(model.predict([7]))
# plt.scatter(x_test, y_test)
# plt.plot()
