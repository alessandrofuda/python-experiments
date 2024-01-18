# SELECT / FILTER  ROWS/COLS DataFrame with pandas lib

# syntax: df.loc[[rows, cols]]  --> double square bracket

# loc --> label-based
# iloc --> integer position-based
import pandas as pd

df = pd.read_csv('data/salaries-2023.csv')  # , index_col=['city']

# basic usage example to x/y modelling
x = df.iloc[:, :-1]
y = df.iloc[:, -1]

# 1 - loc[]
# query/filter rows (1st param)
print(df.loc[df['language'] == 'php'])  # only FIRST param --> only ROWS filter
print(df.loc[(df['language'] == 'php') & (df['city'] == 'Vilnius')])

print(df.loc[0:5, ['language', 'city']])

# 2 - iloc[]
print(df.iloc[0, 0])  # get 1st value up/sx
print(df.iloc[0:4, 2:4])  # important: switching by just two cols



# print(df)
# print(df.head())
# print(x)
