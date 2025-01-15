# FEATURE PREPROCESSING AND SCALING
# Different ways to transform features for machine learning using sklearn

import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler, MinMaxScaler, RobustScaler
from sklearn.preprocessing import OneHotEncoder, LabelEncoder

# Create sample dataset
data = {
    'age': [25, 45, 30, 35, 60],
    'salary': [45000, 90000, 61000, 65000, 120000],
    'department': ['Sales', 'Engineering', 'Sales', 'Marketing', 'Engineering'],
    'experience_level': ['Junior', 'Senior', 'Mid', 'Mid', 'Senior']
}

df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)
print("\n")

# NUMERICAL SCALING METHODS

# 1. StandardScaler (Z-score normalization)
# Transforms features to have mean=0 and variance=1
# Good for algorithms sensitive to magnitudes (like neural networks)
scaler = StandardScaler()
numeric_cols = ['age', 'salary']
scaled_data = scaler.fit_transform(df[numeric_cols])
df_scaled = pd.DataFrame(scaled_data, columns=numeric_cols)
print("StandardScaler Results:")
print(df_scaled)
print("\n")

# 2. MinMaxScaler
# Scales features to a fixed range - usually [0, 1]
# Good for neural networks and algorithms requiring bounded values
minmax = MinMaxScaler()
minmax_data = minmax.fit_transform(df[numeric_cols])
df_minmax = pd.DataFrame(minmax_data, columns=numeric_cols)
print("MinMaxScaler Results:")
print(df_minmax)
print("\n")

# 3. RobustScaler
# Uses statistics that are robust to outliers
# Good for data with outliers
robust = RobustScaler()
robust_data = robust.fit_transform(df[numeric_cols])
df_robust = pd.DataFrame(robust_data, columns=numeric_cols)
print("RobustScaler Results:")
print(df_robust)
print("\n")

# CATEGORICAL ENCODING

# 1. OneHotEncoder
# Creates binary columns for each category
# Good for nominal categorical variables
onehot = OneHotEncoder(sparse_output=False)
categorical_data = onehot.fit_transform(df[['department']])
onehot_cols = onehot.get_feature_names_out(['department'])
df_onehot = pd.DataFrame(categorical_data, columns=onehot_cols)
print("OneHotEncoder Results:")
print(df_onehot)
print("\n")

# 2. LabelEncoder
# Converts categories to integer values
# Good for ordinal categorical variables
label_enc = LabelEncoder()
df['experience_encoded'] = label_enc.fit_transform(df['experience_level'])
print("LabelEncoder Results:")
print(df[['experience_level', 'experience_encoded']])

# WHEN TO USE WHICH SCALER:
# StandardScaler: 
# - When data is approximately normally distributed
# - For algorithms assuming zero mean and unit variance

# MinMaxScaler:
# - When you need bounded values
# - For neural networks or algorithms requiring positive values

# RobustScaler:
# - When you have outliers
# - When you want to preserve zero entries in sparse data

# WHEN TO USE WHICH ENCODER:
# OneHotEncoder:
# - For nominal categories (no inherent order)
# - When cardinality (number of unique values) is manageable

# LabelEncoder:
# - For ordinal categories (have natural order)
# - When you need to preserve order information
