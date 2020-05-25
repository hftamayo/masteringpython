#! /bin/python3
#multidimensional array or list
#it's a list of list

#4 weeks worth of price data points
mpd = [
    [4.5, 4.2, 4.6, 5.1, 4.8], 
    [4.3, 4.9, 5.1, 5.1, 4.8], 
    [4.2, 4.7, 5.2, 5.4, 4.9], 
    [4.6, 4.8, 4.6, 5.7, 4.9]]     

fwd = mpd[0]
print(fwd)
fwd.append(5.5)
print(fwd)    
#el valor que acabo de agregar a la lista tambien esta en la matriz
print(mpd)

#agregando elementos a la matriz
mpd.append([1, 2, 3, 4, 5])
print(mpd)

#acceso a fila y columna especifica: 4.7 fila 2, column 1
print(mpd[2][1])

#reemplazar una lista entera
mpd[3] = [0, 1, 2, 3, 4]
print(mpd)