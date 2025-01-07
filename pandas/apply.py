# .apply()

# Allows you to apply a function to each element, row, or column.

import pandas as pd

df = pd.DataFrame({
    'A': [1, 2, 3],
    'B': [4, 5, 6]
    })

# Apply a function to a single column

df['A'] = df['A'].apply(lambda x: x + 1)

# Or to an entire dataframe
def multiply_by_two(row):
    return row * 2

df = df.apply(multiply_by_two)

print(df)

#########

# Apply with an axis parameter to change it to column

# axis = 0 means column
# axis = 1 means row

df = pd.DataFrame({
    'name': ['alice','bob','jim'],
    'age': [25,30,20]
    })

df['name'] = df['name'].apply(str.upper)

print(df)
