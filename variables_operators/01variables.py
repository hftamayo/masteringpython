#! /bin/python3

stock_name = 'HOOLI'
number_shares = 100
stock_price = 171.06
is_market_open = True
extra_shares = None #tipo de datos especial, similar a Null

#imprimir la variable y su tipo
print("NOMBRE VARIABLE -------------  TIPO------------------ VALOR")
print("stock_name   ", type(stock_name), "    ", stock_name)
print("number_shares   ", type(number_shares), "    ", number_shares)
print("stock_price   ", type(stock_price), "    ", stock_price)
print("is_market_open   ", type(is_market_open), "    ", is_market_open)
print("extra_shares   ", type(extra_shares), "    ", extra_shares)

print("numeros convertidos a cadenas")
print("NOMBRE VARIABLE -------------  TIPO------------------ VALOR")
print("number_shares   ", type(str(number_shares)), "    ", number_shares)
print("stock_price   ", type(str(stock_price)), "    ", stock_price)