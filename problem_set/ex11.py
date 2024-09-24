#  Write a program which asks for two strings,
#  checks if the former contains the latter as a substring,
# and outputs a corresponding message.




user_input_1 = input('Enter a string: ')
user_input_2 = input('Enter a string: ')

if user_input_2 in user_input_1:

    print('The former string contains the latter as a substring.')

else:

    print('The former string does NOT contain the latter as a substring.')




