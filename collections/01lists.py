#! /bin/python3

#stock watchlist
sl = ['Apple', 'microsoft', 'amazon', 'abc']
print(sl)

#longitud de la lista
len(sl)
#agregar elemento
sl.append('Google')
print(sl)
#insertar un elemento en una posicion especifica
sl.insert(1, 'alibaba')
print(sl)
#borrar un item especifico usando el index
del(sl[3])
#sl.pop(3) hace lo mismo
print(sl)
#borrar un item por su contenido
sl.remove('Apple')
print(sl)
#devuelve el numero de coincidencias de un valor en la lista
print(sl.count('alibaba'))