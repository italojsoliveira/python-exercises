
# Write a program that receives an amount in the US dollar from the user and outputs a message saying the respective amount in BRL
# Get the currency rate by scraping a website

import requests

from bs4 import BeautifulSoup

URL = "https://www.forbes.com/advisor/money-transfer/currency-converter/usd-brl/"

page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

html_USD_BRL = soup.find('strong')

value_USD_BRL = float(html_USD_BRL.text.split()[3])

user_dollar = float(input('Enter an amount in the US dollar: '))

print('With $ {} you can buy R$ {}'.format(user_dollar, user_dollar * value_USD_BRL))