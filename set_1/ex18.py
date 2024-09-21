# Create a list with pseudo-random numbers
# Check if all elements in this list are unique

import random as rd

my_list = []

for i in range(0,10):
    my_list.append(rd.randint(0,100))

print(my_list)
if len(my_list) == len(set(my_list)):
    print("All elements in this list are unique!")
else:
    print("Not all elements in this list are unique!")

