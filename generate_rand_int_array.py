# Generate random array
import random
import numpy as np

# 1st method
X = []
for i in range(10):
    X.append(random.randint(0, 1000))

print(X)
print(type(X))
# print(X[2:5])

# 2nd method
Y = np.random.randint(0, 1000, 10).tolist()
print(Y)
print(type(Y))
