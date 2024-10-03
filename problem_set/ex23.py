# Palindrome is a word, phrase, or sequence that reads the same backwards as forwards, e.g. madam or nurses run.
# Checking if a string is a palindrome

my_string =input('Enter a string to check if it is a palindrome: ')

if my_string[::-1] == my_string:
    print(my_string, "is a palindrome.")
else:
    print(my_string, "is not a palindroe.")