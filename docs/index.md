---
title: Home
layout: home
---

# Exercises with Solutions in Python

[![](https://img.shields.io/badge/-Python-grey?&logo=Python)](https://www.python.org/)
 [![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

Coding exercises and solutions in Python. They are code snippets that may be useful for everyday tasks.

_This is a work in progress_. The last commit shows the latest updates.

## Table of Contents

- [Exercises with Solutions in Python](#exercises-with-solutions-in-python)
  - [Table of Contents](#table-of-contents)
    - [Exercise 1: Input/output strings](#exercise-1-inputoutput-strings)
    - [Exercise 2: Some Boolean string methods](#exercise-2-some-boolean-string-methods)
    - [Exercise 3: Input/output numbers](#exercise-3-inputoutput-numbers)
    - [Exercise 4: Formatting strings](#exercise-4-formatting-strings)
    - [Exercise 5: Computing the average grade](#exercise-5-computing-the-average-grade)
    - [Exercise 6: Distance conversions](#exercise-6-distance-conversions)
    - [Exercise 7: Multiplication table](#exercise-7-multiplication-table)
    - [Exercise 8: Currency conversion using web scrapping](#exercise-8-currency-conversion-using-web-scrapping)
    - [Exercise 9: Counting string characters and storing in a dictionary](#exercise-9-counting-string-characters-and-storing-in-a-dictionary)
    - [Exercise 10](#exercise-10)
    - [Exercise 11](#exercise-11)
    - [Exercise 12](#exercise-12)
    - [Exercise 13](#exercise-13)
    - [Exercise 14](#exercise-14)
    - [Exercise 15](#exercise-15)
    - [Exercise 16](#exercise-16)
    - [Exercise 17](#exercise-17)
    - [Exercise 18](#exercise-18)
    - [Exercise 19](#exercise-19)
    - [Exercise 20](#exercise-20)
    - [Exercise 21](#exercise-21)
    - [Exercise 22](#exercise-22)
    - [Exercise 23](#exercise-23)
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

```
</details>

### Exercise 10

 Write a program that asks for a string and outputs the reverse of it.


<details markdown=block>
<summary markdown=span>Click here to see a possible solution</summary>

```python
user_input = input('Enter a string: ')

print(user_input[::-1])
```
</details>

### Exercise 11

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


### Exercise 12

Create a list composed by pseudo-random integer numbers and find the maximum value in it.

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

### Exercise 13

Create a list composed by pseudo-random integer numbers and find the index of the maximum value in it.

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

### Exercise 14

<details markdown=block>
<summary markdown=span>Click here to see a possible solution</summary>

Create a list and reverse it.

```python
list_variable = [1, 2, 3, 4, 5]

reverse_list = list_variable[::-1]

print(reverse_list)
```
</details>


### Exercise 15

Sorting a dictionary by value

### Exercise 16

Checking if a file exists

### Exercise 17

Counting the occurrence of an item in a list

### Exercise 18

Checking if all elements in a list are unique

### Exercise 19

Removing the occurrence of an item in a list

### Exercise 20

Flattening a nested list

### Exercise 21

Merging two dictionaries

### Exercise 22

Removing all whitespace from a string

### Exercise 23

Checking if a string is a palindrome

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