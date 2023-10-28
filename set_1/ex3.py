
# Write a program that reads the user input number and outputs a message saying its antecedent and successor.

user_input = int(input('Enter a number: '))

antecedent = user_input - 1

successor = user_input + 1

print('By analyzing number {}, its antecedent is {} and its successor is {}.'.format(user_input, antecedent, successor))