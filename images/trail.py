import pandas as pd

# create a sample dataset
df = pd.DataFrame({'name': ['Alice', 'Bob', 'Charlie'],
                   'age': [25, 30, 35],
                   'city': ['New York', 'London', 'Paris']})

idx = df.index[df['name'] == 'Bob'][0]
print(idx)
name = df.iloc[1]['city']
print(name)

#
