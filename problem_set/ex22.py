# Removing all whitespace from a string

my_string = "   hello    world    "
print(my_string)
new_string = "".join(my_string.split())
print(new_string)