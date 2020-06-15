#! /bin/python3
#
nos = 5

def buyshares():
    #no se recomienda usar variables globales
    global nos
    nos +=1
    print(nos)

for _ in range(0,5):
    buyshares()
