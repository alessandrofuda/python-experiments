# to understand the base of data via Pandas library
import pandas as pd

df = pd.read_csv('data/huge.csv')

# very general info: rows & cols
print(df.shape)

# cols name, non-null values, values types, memory usage,..
print(df.info())

# only for int columns: count, mean, standard deviation, min, percentiles, max, ..
print(df.describe())

# to show first/last five rows or random
print(df.head())
print(df.head(3))
print(df.tail())
print(df.sample(4))

# the n highest/lower values in column
print(df.nlargest(5, 'dddddddd'))
print(df.nsmallest(5, 'dddddddd'))

# group by column dddddddd and count how many values per group
print(df.dddddddd.value_counts())
print(df.dddddddd.value_counts(normalize=True))  # same but in %
print(df[['dddddddd']].mean())
print(df.groupby('col1')[['col2']].mean())
