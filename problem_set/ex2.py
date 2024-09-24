# Write a program that reads the user input and outputs the following pieces of information about it:

# - Does it have only space?

# - Is it a number?

# - Is it alphabetic?

# - Is it alphanumeric?

# - Is it in uppercase?

# - Is it in lowercase?

# - Is it capitalized?


user_input = input('Enter something: ')

print('The Python primitive datatype of this value is', type(user_input))

print('Does it have only space?', user_input.isspace())

print('Is it a number?', user_input.isnumeric())

print('Is it alphabetic?', user_input.isalpha())

print('Is it alphanumeric?', user_input.isalnum())

print('Is it in uppercase?', user_input.isupper())

print('Is it in lowercase?', user_input.islower())

print('Is it capitalized?', user_input.istitle())

