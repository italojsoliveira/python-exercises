# Flattening a nested list

my_list = [[1,2], [3,4], [5,6]]
flattened_list = [x for sublist in my_list for x in sublist]
print(flattened_list)