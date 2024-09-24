# Write a program which counts and print the numbers of each character in a string input given by the user.
# The outcome should be a dictionary.
# For example, for the input 'abcdefgabc', the output should be {'a':2, 'c':2, 'b':2, 'e':1, 'd':1, 'g':1, 'f':1}

user_input = input('Enter a string: ')

count = dict()

for string in user_input:

    count[string] = count.get(string, 0) + 1

print(count)