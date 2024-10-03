---
title: Home
layout: home
---

# Exercises with Solutions in Python

[![](https://img.shields.io/badge/-Python-grey?&logo=Python)](https://www.python.org/)
 [![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

Coding exercises and solutions in Python. They are code snippets that may be useful for everyday tasks.

_This is a work in progress_. The last commit shows the latest updates.

- [Exercises with Solutions in Python](#exercises-with-solutions-in-python)
    - [Exercise 1: Input/output strings](#exercise-1-inputoutput-strings)
    - [Exercise 2: Some Boolean string methods](#exercise-2-some-boolean-string-methods)
    - [Exercise 3: Input/output numbers](#exercise-3-inputoutput-numbers)
    - [Exercise 4: Formatting strings](#exercise-4-formatting-strings)
    - [Exercise 5: Computing the average grade](#exercise-5-computing-the-average-grade)
    - [Exercise 6: Distance conversions](#exercise-6-distance-conversions)
    - [Exercise 7: Multiplication table](#exercise-7-multiplication-table)
    - [Exercise 8: Currency conversion using web scrapping](#exercise-8-currency-conversion-using-web-scrapping)
    - [Exercise 9: Counting string characters and storing in a dictionary](#exercise-9-counting-string-characters-and-storing-in-a-dictionary)
    - [Exercise 10: Reversing a string](#exercise-10-reversing-a-string)
    - [Exercise 11: Checking substrings](#exercise-11-checking-substrings)
    - [Exercise 12: Pseudo-random integers and maximum value](#exercise-12-pseudo-random-integers-and-maximum-value)
    - [Exercise 13: Pseudo-random integers and index](#exercise-13-pseudo-random-integers-and-index)
    - [Exercise 14: Reversing a list](#exercise-14-reversing-a-list)
    - [Exercise 15: Sorting a dictionary by value with pseudo-random numbers](#exercise-15-sorting-a-dictionary-by-value-with-pseudo-random-numbers)
    - [Exercise 16: Checking if a file exists](#exercise-16-checking-if-a-file-exists)
    - [Exercise 17: Counting the occurrence of each item in the list](#exercise-17-counting-the-occurrence-of-each-item-in-the-list)
    - [Exercise 18: Checking if all elements in a list are unique](#exercise-18-checking-if-all-elements-in-a-list-are-unique)
    - [Exercise 19: Removing all occurrences of an item from a list](#exercise-19-removing-all-occurrences-of-an-item-from-a-list)
    - [Exercise 20: Flattening a nested list](#exercise-20-flattening-a-nested-list)
    - [Exercise 21: Merging two dictionaries](#exercise-21-merging-two-dictionaries)
    - [Exercise 22: Removing all whitespace from a string](#exercise-22-removing-all-whitespace-from-a-string)
    - [Exercise 23: Checking if a string is a palindrome](#exercise-23-checking-if-a-string-is-a-palindrome)
    - [Exercise 24](#exercise-24)
    - [Exercise 25](#exercise-25)
    - [Exercise 26](#exercise-26)


### Exercise 1: Input/output strings

Write a program that reads the user name as an input and outputs a welcome message.

<details markdown=block>
<summary markdown=span>Click here to see a possible solution</summary>

```python
user_name = input('Write your first name: ')
print('Welcome,', user_name, '!')
print('Welcome, {}!'.format(user_name))
```
</details>


### Exercise 2: Some Boolean string methods

Write a program that reads the user input and outputs the following pieces of information about it:

- Does it have only space?

- Is it a number?

- Is it alphabetic?

- Is it alphanumeric?

- Is it in uppercase?

- Is it in lowercase?

- Is it capitalized?

<details markdown=block>
<summary markdown=span>Click here to see a possible solution</summary>

```python
user_input = input('Enter something: ')
print('The Python primitive datatype of this value is', type(user_input))
print('Does it have only space?', user_input.isspace())
print('Is it a number?', user_input.isnumeric())
print('Is it alphabetic?', user_input.isalpha())
print('Is it alphanumeric?', user_input.isalnum())
print('Is it in uppercase?', user_input.isupper())
print('Is it in lowercase?', user_input.islower())
print('Is it capitalized?', user_input.istitle())
```
</details>

### Exercise 3: Input/output numbers

Write a program that reads the user input number and outputs a message saying its antecedent and successor.

<details markdown=block>
<summary markdown=span>Click here to see a possible solution</summary>

```python
user_input = int(input('Enter a number: '))
antecedent = user_input - 1
successor = user_input + 1
print('By analyzing number {}, its antecedent is {} and its successor is {}.'.format(user_input, antecedent, successor))
```
</details>

### Exercise 4: Formatting strings

Write a program that reads the user input number and outputs a message saying its double, triple, and square root with at most two decimal digits.

<details markdown=block>
<summary markdown=span>Click here to see a possible solution</summary>

```python
user_input = int(input('Enter a number: '))
print(  'The double of {} is {}.'.format(user_input, 2 * user_input)  )
print(  'The triple of {} is {}.'.format(user_input, 3 * user_input)  )
print(  'The square root of {} is {:.2f}.'.format(user_input, user_input ** 0.5)  )
```
</details>

### Exercise 5: Computing the average grade

Write a program that receives two student grades and outputs the average grade.

<details markdown=block>
<summary markdown=span>Click here to see a possible solution</summary>

```python
grade_1 = float(input('Enter the first grade: '))
grade_2 = float(input('Enter the second grade: '))
print('The first student grade is {}.'.format(grade_1))
print('The second student grade is {}.'.format(grade_2))
print('The average between {} and {} is {}'.format(grade_1, grade_2, (grade_1 + grade_2)/2))
```
</details>

### Exercise 6: Distance conversions

Write a program that receives a distance value in meters and outputs a message saying its corresponding values in km, hm, dam, dm, cm, and mm.

<details markdown=block>
<summary markdown=span>Click here to see a possible solution</summary>

```python
meter_distance = float(input('Enter the distance in meters: '))
km_distance = meter_distance / 1000
hm_distance = meter_distance / 100
dam_distance = meter_distance / 10
dm_distance = meter_distance * 10
cm_distance = meter_distance * 100
mm_distance = meter_distance * 1000
print('The measure of {} m correspond to \n {} km \n {} hm \n {} dam \n {} dm \n {} cm \n {} mm'.format(meter_distance, km_distance,
                                                                                                        hm_distance, dam_distance, dm_distance, cm_distance, mm_distance))
```
</details>

### Exercise 7: Multiplication table

Write a program that receives a number and gives its multiplication table like this:

    ------------
    3 x 1 = 3
    3 x 2 = 6
    3 x 3 = 9
    3 x 4 = 12
    3 x 5 = 15
    3 x 6 = 18
    3 x 7 = 21
    3 x 8 = 24
    3 x 9 = 27
    3 x 10 = 30
    ------------

<details markdown=block>
<summary markdown=span>Click here to see a possible solution</summary>

```python
user_input_number = int(input('Enter a number to see its multiplication table: '))
print('-' * 12)
print('{} x 1 = {}'.format( user_input_number, user_input_number * 1 ))
print('{} x 2 = {}'.format( user_input_number, user_input_number * 2 ))
print('{} x 3 = {}'.format( user_input_number, user_input_number * 3 ))
print('{} x 4 = {}'.format( user_input_number, user_input_number * 4 ))
print('{} x 5 = {}'.format( user_input_number, user_input_number * 5 ))
print('{} x 6 = {}'.format( user_input_number, user_input_number * 6 ))
print('{} x 7 = {}'.format( user_input_number, user_input_number * 7 ))
print('{} x 8 = {}'.format( user_input_number, user_input_number * 8 ))
print('{} x 9 = {}'.format( user_input_number, user_input_number * 9 ))
print('{} x 10 = {}'.format( user_input_number, user_input_number * 10 ))
print('-' * 12)
```
</details>

### Exercise 8: Currency conversion using web scrapping

Write a program that receives an amount in the US dollar from the user and outputs a message saying the respective amount in BRL. Get the currency rate by scraping a website.

<details markdown=block>
<summary markdown=span>Click here to see a possible solution</summary>

```python
import requests
from bs4 import BeautifulSoup
URL = "https://www.forbes.com/advisor/money-transfer/currency-converter/usd-brl/"
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")
html_USD_BRL = soup.find('strong')
value_USD_BRL = float(html_USD_BRL.text.split()[3])
user_dollar = float(input('Enter an amount in the US dollar: '))
print('With $ {} you can buy R$ {}'.format(user_dollar, user_dollar * value_USD_BRL))
```
</details>

### Exercise 9: Counting string characters and storing in a dictionary 

Write a program which counts and print the numbers of each character in a string input given by the user. The outcome should be a dictionary. For example, for the input 'abcdefgabc', the output should be {'a':2, 'c':2, 'b':2, 'e':1, 'd':1, 'g':1, 'f':1}

<details markdown=block>
<summary markdown=span>Click here to see a possible solution</summary>

```python
user_input = input('Enter a string: ')

count = dict()

for string in user_input:

    count[string] = count.get(string, 0) + 1

print(count)

```
</details>

### Exercise 10: Reversing a string

 Write a program that asks for a string and outputs the reverse of it.


<details markdown=block>
<summary markdown=span>Click here to see a possible solution</summary>

```python
user_input = input('Enter a string: ')

print(user_input[::-1])
```
</details>

### Exercise 11: Checking substrings

 Write a program which asks for a string, checks if it contains a substring, and outputs a corresponding message.

<details markdown=block>
<summary markdown=span>Click here to see a possible solution</summary>

```python
user_input_1 = input('Enter a string: ')
user_input_2 = input('Enter a string: ')

if user_input_2 in user_input_1:

    print('The former string contains the latter as a substring.')

else:

    print('The former string does NOT contain the latter as a substring.')

```
</details>


### Exercise 12: Pseudo-random integers and maximum value

Create a list composed of pseudo-random integer numbers and find the maximum value in it.

<details markdown=block>
<summary markdown=span>Click here to see a possible solution</summary>

```python
import random

list_variable = []

# appending 10000 pseudo-random numbers (ranging between 0 and 10000000) to a list
for i in range(0,1000):
    list_variable.append(random.randint(0,10000000))

print('The maximum integer of the "list_variable" list is', max(list_variable))

```
</details>

### Exercise 13: Pseudo-random integers and index

Create a list composed of pseudo-random integer numbers and find the index of the maximum value in it.

<details markdown=block>
<summary markdown=span>Click here to see a possible solution</summary>

```python
import random

list_variable = []

# appending 10000 pseudo-random numbers (ranging between 0 and 10000000) to a list
for i in range(0,1000):
    list_variable.append(random.randint(0,10000000))

print('The index of the maximum integer of the "list_variable" list is', list_variable.index(max(list_variable)))

```
</details>

### Exercise 14: Reversing a list

Create a program that reverses a list.

<details markdown=block>
<summary markdown=span>Click here to see a possible solution</summary>

```python
list_variable = [1, 2, 3, 4, 5]

reverse_list = list_variable[::-1]

print(reverse_list)
```
</details>


### Exercise 15: Sorting a dictionary by value with pseudo-random numbers

Create a dictionary with four keys, each having a pseudo-random integer as its value. Sort the dictionary by value.

<details markdown=block>
<summary markdown=span>Click here to see a possible solution</summary>

```python
import random

points = {
    "Mary": random.randint(0, 100000), "John": random.randint(0, 100000),
    "Teresa": random.randint(0, 100000), "Peter": random.randint(0, 100000)
    }

sorted_dict = {
    k: v for k, v in sorted(points.items(), key=lambda item: item[1])
}

print(sorted_dict)
```
</details>

### Exercise 16: Checking if a file exists

Create a program that check if a file exists in a directory.

<details markdown=block>
<summary markdown=span>Click here to see a possible solution</summary>

```python
import os

if os.path.isfile("file.txt"):
    print("File exists!")
else:
    print("File does not exists!")
```
</details>

### Exercise 17: Counting the occurrence of each item in the list

Create a list with pseudo-random numbers. Count the occurrence of each item in the list and store the result in a dictionary.

<details markdown=block>
<summary markdown=span>Click here to see a possible solution</summary>

```python
import random

my_list = []

for i in range(0,100):
    my_list.append(random.randint(0,10))

# Create an empty dictionary to store the counts
element_count = {}

# Iterate through the list and count occurrences
for element in my_list:
    if element in element_count:
        element_count[element] += 1
    else:
        element_count[element] = 1

print(element_count)
```
</details>

### Exercise 18: Checking if all elements in a list are unique

Create a list with pseudo-random integer numbers. Then, check if all elements in this list are unique or not.

<details markdown=block>
<summary markdown=span>Click here to see a possible solution</summary>

```python
import random as rd

my_list = []

for i in range(0,10):
    my_list.append(rd.randint(0,100))

print(my_list)
if len(my_list) == len(set(my_list)):
    print("All elements in this list are unique!")
else:
    print("Not all elements in this list are unique!")
```
</details>

### Exercise 19: Removing all occurrences of an item from a list

Create a program that removes all occurrences of an item from a list.

<details markdown=block>
<summary markdown=span>Click here to see a possible solution</summary>

```python
my_list = [1, 2, 3, 4, 5, 6, 3, 1]
item = 1
my_new_list = [x for x in my_list if x != item]
print(my_list, "\n", my_new_list)
```
</details>

### Exercise 20: Flattening a nested list

Create a program that flattens a nested list.

<details markdown=block>
<summary markdown=span>Click here to see a possible solution</summary>

```python
my_list = [[1,2], [3,4], [5,6]]
flattened_list = [x for sublist in my_list for x in sublist]
print(flattened_list)
```
</details>

### Exercise 21: Merging two dictionaries

Create a program that merges two dictionaries.

<details markdown=block>
<summary markdown=span>Click here to see a possible solution</summary>

```python
dict1 = {'apple': 3, 'banana': 1}
dict2 = {'orange':2, 'pear': 4}
merged_dict = {**dict1, **dict2}
print(merged_dict)
```
</details>

### Exercise 22: Removing all whitespace from a string

Create a program that removes all whitespace from a string.

<details markdown=block>
<summary markdown=span>Click here to see a possible solution</summary>

```python
my_string = "   hello    world    "
print(my_string)
new_string = "".join(my_string.split())
print(new_string)
```
</details>

### Exercise 23: Checking if a string is a palindrome

Palindrome is a word, phrase, or sequence that reads the same backwards as forwards, e.g. madam or nurses run. Write a program that checks if an arbitrary string is a palindrome.

<details markdown=block>
<summary markdown=span>Click here to see a possible solution</summary>

```python
my_string =input('Enter a string to check if it is a palindrome: ')
if my_string[::-1] == my_string:
    print(my_string, "is a palindrome.")
else:
    print(my_string, "is not a palindroe.")
```
</details>

### Exercise 24

Removing duplicates from a string

### Exercise 25

Counting the number of words in a string

### Exercise 26

Generating a random integer


```mermaid
graph TD;
    A-->B;
    A-->C;
    B-->D;
    C-->D;
```



---