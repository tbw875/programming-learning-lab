# LAMBDA FUNCTIONS

# A Lambda function is a temporary, anonymous function. It is best used when you only need to use the function once, and it is simple logic.

# Setting up an example DataFrame:
import pandas as pd

data = {
        'Recipes':[
            'Apple Pie',
            'Dutch Baby',
            'Pepperoni & Jalapeno Pizza',
            'Lamb Gyro',
            'Ants on a Log'
            ]
        }

df = pd.DataFrame(data)

# This is the function in the traditional sense:
def check_text(text):
	return 'Dutch' in text

df['Recipes'].map(check_text)

# And the same as a lambda function:

df['Recipes'].map(lambda text: 'Dutch' in text)


###########

# Using Mathematical logic:

# Create a lambda function that checks if a number is between 1 and 10
in_range = lambda x: 1 <= x <= 10

# Test it with different numbers
numbers = [0, 5, 10, 15]
results = list(map(in_range, numbers))

print(results)  # Output: [False, True, True, False]

###########

# Another Example:

# Lambda function to calculate the hypotenuse of a right triangle
hypotenuse = lambda a, b: (a**2 + b**2)**0.5

# Test it
print(hypotenuse(3, 4))  # Output: 5.0
print(hypotenuse(1, 1))  # Output: ~1.414 (√2)
