# GROUP BY

# Allows you to aggregate rows within a dataframe into groups that you specify.
import pandas as pd

df = pd.DataFrame({
    'category': ['A','A','B','B'],
    'value': [1, 2, 3, 4]
    })

# Sum the values for each category type
grouped = df.groupby('category').sum()

print(grouped)
