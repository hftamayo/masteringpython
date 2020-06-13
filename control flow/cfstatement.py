#! /bin/python3
# sell off negative stocks and keep positive ones

sdict = {'AAPL': False, 'MSFT': True, 'AMZN': False}

for item in list(sdict.items()):
    is_positive = item[1]
    if is_positive:
        continue
    print(f'Sold sharersof {item[0]}')

bs = 5
nos = 22

while nos > 0:
    if nos < 5:
        break
    nos -= bs
    print(f'We still have {nos} shares left')