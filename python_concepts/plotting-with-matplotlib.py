import pandas as pd
import matplotlib.pyplot as plt

# Create sample data
data = {
    'date': pd.date_range(start='2024-01-01', periods=12, freq='M'),
    'sales': [45, 52, 48, 58, 67, 72, 75, 71, 68, 77, 82, 88],
    'customers': [120, 125, 118, 132, 141, 145, 152, 148, 143, 155, 162, 170]
}

# Create DataFrame
df = pd.DataFrame(data)

# Create a figure with two subplots
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8))

# Plot sales over time
ax1.plot(df['date'], df['sales'], marker='o', color='blue')
ax1.set_title('Monthly Sales')
ax1.grid(True)

# Plot customers over time
ax2.plot(df['date'], df['customers'], marker='s', color='green')
ax2.set_title('Monthly Customers')
ax2.grid(True)

plt.tight_layout()
plt.show()
