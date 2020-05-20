#! /bin/python3
#almacenan valores relacionados, pero no en gran cantidad
#almacenan multiples tipos de datos
#get, not set, individual elements
#fewer operations

stock_purchase = ('Apple', 171.06, 100)
print(stock_purchase)
sn = stock_purchase[0]
print(sn)
#stock_purchase[2] = 150 esta linea no funciona porque no se permite reasignar valores
print(len(stock_purchase))
#obtener el indice de un valor
print(stock_purchase.index(100))
#contar el numero de coincidencias de un valor
print(stock_purchase.count(171.06))
