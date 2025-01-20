# List Comprehension

# A quick way to work with lists by creating pythonic code within the list itself

# Example 1

squares = []
for x in range(10):
    squares.append(x**2)
    # This returns each square value of x, a value between 1 and 10

# Instead with list comprehension we can write it much easier:

squares = [x**2 for x in range(10)]
print(squares)

# This combines the for loop with the expression within the loop.

#####
# Example 2: Given a list of strings, evaluate if it has the vowel "a" in it, and if so, add it to the new list

# without comprehension:
fruits = ['apple','banana','cherry','kiwi','mango']
new_list = []

for x in fruits:
    if "a" in x:
        new_list.append(x)

print(new_list)

# with list comprehension:

new_list = [x for x in fruits if "a" in x]
# [x : give me the value "apple"
# for x in fruits: loop to iterate over
# if "a" in x] : conditional to evaluate

# or as w3 schools says it:
# newlist = [expression for item in iterable if condition == True]
