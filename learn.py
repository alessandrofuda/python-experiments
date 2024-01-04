# print('sdjhgdfsj')
import pandas as pd
df = pd.read_csv('salaries.csv')
df.head()
x = df.iloc[:,:-1]
print(x)

