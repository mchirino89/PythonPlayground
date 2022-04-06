pesos = input("How many pesos (uy) do you have?: ")
pesos = float(pesos)
dolarExchangeRate = 43.25
amountInDolars = pesos / dolarExchangeRate
amountInDolars = str(amountInDolars)
print("You have $" + amountInDolars + " dolars")