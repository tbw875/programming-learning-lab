# RESHAPING DATA WITH MELT AND PIVOT
# While pivot() spreads data into columns, melt() does the opposite - 
# it converts columns into rows, making wide data longer.

import pandas as pd

# Create a sample DataFrame representing sales data
# This is in "wide" format, with each product as a column
data = {
    'store': ['Store A', 'Store B', 'Store C'],
    'chips': [100, 150, 200],
    'soda': [200, 300, 400],
    'candy': [50, 75, 100]
}

df = pd.DataFrame(data)
print("Original DataFrame (wide format):")
print(df)
print("\n")

# MELT EXAMPLE
# melt() transforms columns into rows
# Useful when you have variables spread across columns and want to consolidate them

melted_df = df.melt(
    id_vars=['store'],              # Column(s) to keep as identifier
    value_vars=['chips', 'soda', 'candy'],  # Columns to convert to rows
    var_name='product',             # Name for the column containing old column names
    value_name='sales'              # Name for the column containing values
)
print("Melted DataFrame (long format):")
print(melted_df)
print("\n")

# PIVOT EXAMPLE
# pivot() does the opposite of melt() - it spreads data from rows into columns
# Let's add some time data to make it more interesting
melted_df['quarter'] = ['Q1', 'Q1', 'Q1', 'Q2', 'Q2', 'Q2', 'Q3', 'Q3', 'Q3']

print("Melted DataFrame with time data:")
print(melted_df)
print("\n")

# Now pivot to see sales by store and product across quarters
pivoted_df = melted_df.pivot(
    index='store',      # Row labels
    columns='quarter',  # Column labels
    values='sales'      # Values to aggregate
)
print("Pivoted DataFrame:")
print(pivoted_df)

# PRACTICAL USE CASES:
# melt() is useful when:
# - Converting wide data to long format for time series analysis
# - Preparing data for visualization with libraries like seaborn
# - Normalizing data structure for machine learning

# pivot() is useful when:
# - Creating summary tables
# - Generating cross-tabulations
# - Reshaping data for reporting or analysis
