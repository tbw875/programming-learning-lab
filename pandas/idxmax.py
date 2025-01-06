# .idxmax()

# A pandas method that returns the index label of the first maximum value in a Series or a DataFrame.

import pandas as pd

series = pd.Series([10, 20, 15, 30, 25], index=['a','b','c','d','e'])

max_index_in_series = series.idxmax() # returns 'd' since 30

print(f'Example Series: {series}')
print(f'series.idxmax() = {max_index_in_series}')

# If there are multiple maximums, returns first occurance.

# Combine with `groupby()` to find max values within groups
