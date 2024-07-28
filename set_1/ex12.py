#  Create a list composed by pseudo-random integer numbers and find the maximum value in it.

import random

list_variable = []

# appending 10000 pseudo-random numbers (ranging between 0 and 10000000) to a list
for i in range(0,1000):
    list_variable.append(random.randint(0,10000000))

print('The maximum integer of the "list_variable" list is', max(list_variable))