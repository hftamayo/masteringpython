#! /bin/python3
#
sdicts = {'AAPL': 171.62, 'MSFT': 113.45, 'AMZN': 1670.98}

print(list(sdicts.items()))
for item in list(sdicts.items()):
    print(item)
    #uso f para poner las vars en los brackets
    print(f'Stock name: {item[0]}, current price: {item[1]}')

#las siguientes lineas hacen lo mismo pero con mas lineas
sdl = list(sdicts.items())
for i in range(0, len(sdl)):
    stuple = sdl[i]
    print(f'Stock name: {stuple[0]}, current price: {stuple[1]}')

#_ indica que el indice puede ser cualquier porcion de la RAM
for _ in range(0, 5):
    print('python is great')