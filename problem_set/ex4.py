
# Write a program that reads the user input number and outputs a message saying its double,
# triple, and square root with at most two decimal digits.


user_input = int(input('Enter a number: '))

print(  'The double of {} is {}.'.format(user_input, 2 * user_input)  )

print(  'The triple of {} is {}.'.format(user_input, 3 * user_input)  )

print(  'The square root of {} is {:.2f}.'.format(user_input, user_input ** 0.5)  )
