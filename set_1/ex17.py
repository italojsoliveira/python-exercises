# Create a list with random numbers.
# Count the occurrence of each item in the list and store the result in a dictionary

import random

my_list = []

for i in range(0,100):
    my_list.append(random.randint(0,10))

# Create an empty dictionary to store the counts
element_count = {}

# Iterate through the list and count occurrences
for element in my_list:
    if element in element_count:
        element_count[element] += 1
    else:
        element_count[element] = 1

print(element_count)