# LIST COMPREHENSIONS
# List comprehensions provide a concise way to create lists based on existing lists/iterables.
# They combine a for loop and list creation into a single line of readable code.

# Setting up example data:
import pandas as pd
data = {
    'Products': [
        'iPhone 13',
        'Samsung TV',
        'Apple Watch',
        'Sony Headphones',
        'iPad Pro'
    ],
    'Prices': [799, 1299, 399, 249, 999]
}
df = pd.DataFrame(data)

# Traditional way to create a list of Apple products:
apple_products = []
for product in df['Products']:
    if 'Apple' in product or 'iPhone' in product or 'iPad' in product:
        apple_products.append(product)
print("Traditional way:", apple_products)

# Same thing using a list comprehension:
apple_products = [product for product in df['Products'] 
                 if 'Apple' in product or 'iPhone' in product or 'iPad' in product]
print("List comprehension:", apple_products)

###########
# Working with numbers:
# Create a list of squared numbers for prices under 500
# Traditional way:
squared_prices = []
for price in df['Prices']:
    if price < 500:
        squared_prices.append(price ** 2)
print("Traditional squared prices:", squared_prices)

# List comprehension way:
squared_prices = [price ** 2 for price in df['Prices'] if price < 500]
print("List comprehension squared prices:", squared_prices)

###########
# Nested list comprehension example:
# Create a matrix of multiplication table
size = 3
multiplication_table = [[i * j for j in range(1, size + 1)] for i in range(1, size + 1)]
print("\nMultiplication table:")
for row in multiplication_table:
    print(row)

###########
# Combining with dictionary comprehension:
# Create a dictionary of product: price for Apple products
apple_prices = {product: price for product, price in zip(df['Products'], df['Prices'])
                if 'Apple' in product or 'iPhone' in product or 'iPad' in product}
print("\nApple product prices:", apple_prices)
