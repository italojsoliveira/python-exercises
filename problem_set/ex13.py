# Create a list composed by pseudo-random integer numbers and find the index of the maximum value in it.

import random

list_variable = []

# appending 10000 pseudo-random numbers (ranging between 0 and 10000000) to a list
for i in range(0,1000):
    list_variable.append(random.randint(0,10000000))

print('The index of the maximum integer of the "list_variable" list is', list_variable.index(max(list_variable)))