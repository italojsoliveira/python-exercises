---
title: Home
layout: home
---

# Exercises with Solutions in Python

[![](https://img.shields.io/badge/-Python-grey?&logo=Python)](https://www.python.org/)
 [![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

Coding exercises and solutions in Python from my studies and practice. Here I make it publicly open for whoever finds it helpful.

I expect to write more than a thousand exercises with solutions. _This is a work in progress_. The last commit shows the latest updates.

### Exercise 1

Write a program that reads the user name as an input and outputs a welcome message.

<details markdown=block>
<summary markdown=span>Click here to see a possible solution</summary>

```python
user_name = input('Write your first name: ')
print('Welcome,', user_name, '!')
print('Welcome, {}!'.format(user_name))
```
</details>


### Exercise 2

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

### Exercise 3

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

### Exercise 4

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

### Exercise 5

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

### Exercise 6

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

### Exercise 7

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

### Exercise 8

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

### Exercise 9

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

### Exercise 10





---