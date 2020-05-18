#! /bin/python3

x = 100

#concatenando con la funcion str
print("Salida de datos con la funcion str: ")
print("Cociente: " + str(x / 3))
print("Parte entera del Cociente: " + str(x // 3))
print("Residuo: " + str(x % 3))

#concatenando con la funcion format
print("Salida de datos con la funcion format: ")
division1 = format(x / 3, '.5f')
division2 = '{:.5f}'.format(x / 3)
print("Cociente 1: " + str(division1))
print("Cociente 2: " + str(division2))
print("Parte entera del Cociente: " + str(x // 3))
print("Residuo: " + str(x % 3))

#acumuladores
x += 50
print("acumulador de variable: " + str(x))
nombre = 'Herbert '
nombre += ' Eduardo'
print(nombre)
booleano = "A" > "B"
print(booleano) #es falso porque A esta mas cerca del inicio del alfabeto

#tipos de variables
print(type(x))
print(type(nombre))
print(type(booleano))

#operadores logicos
print(not booleano)
y = 1
z = x + y
print(z > x and y > x)
print(z > x or y > x)