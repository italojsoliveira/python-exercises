# Removing all occurrences of an item from a list

my_list = [1, 2, 3, 4, 5, 6, 3, 1]
item = 1
my_new_list = [x for x in my_list if x != item]
print(my_list, "\n", my_new_list)