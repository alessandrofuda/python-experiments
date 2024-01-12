import pandas as pd

vehicles = pd.read_csv('~/Code/python_learn/lnkdn/exerc_files/03/vehicles.csv')
print(vehicles.info())

# citympg --> miles per gallon

# relation visualization
print(vehicles.plot(kind='scatter', x='citympg', y='co2emissions'))
# vehicles.show()

# distribution visualization
vehicles['co2emissions'].plot(kind='hist')
# comparision visualization
vehicles.pivot(columns='drive', values='co2emissions')
vehicles.pivot(columns='drive', values='co2emissions').plot(kind='box', figsize=(10,6))
# composition visualization
vehicles.groupby('year')['drive'].value_counts()
vehicles.groupby('year')['drive'].value_counts().unstack().plot(kind='bar', stacked=True, figsize=(10, 6))

