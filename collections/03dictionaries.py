#! /bin/python3
#es una lista de tuples
#key and values pueden ser de cualquier tipo
sdicts = {'Apple':172.59, 'Microsoft': 112.53, 'Amazon': 161.50}
#obtener el precio relacionado a MS, no es seguro hacer esto porque no estoy seguro si existe el  valor
msprice = sdicts['Microsoft']
print(msprice)
#cambiar el valor asignado al elemento Amazon y agregar un nuevo elemento
sdicts['Amazon'] = 170
sdicts['Google'] = 200
print(sdicts)
#forma adecuada de obtener un elemento aun cuando no exista
print(sdicts.get('okokok'))
#len de la estructura
print(len(sdicts))
#borrar un elemento
del(sdicts['Google'])
print(sdicts)
#eliminar un elemento con pop
print(sdicts.pop('Apple'))
#devuelve las tuplas del diccionario
print(list(sdicts.items()))
print(list(sdicts.values()))
print(list(sdicts.keys()))