from forex_python.converter import CurrencyRates

cr = CurrencyRates()

cr.get_rates('USD')

#amount_BRL = int(input("Please enter the amount you want to convert: "))

#amount_USD = cr.convert('BRL', 'USD', amount_BRL)

#print("With R$ {} you can buy $ {} US dollars.".format(amount_BRL, amount_USD))