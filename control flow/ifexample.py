#! /bin/python3
#

sp = 150
action = ''

if sp <= 140:
    action = 'buy'
elif sp >=160:
    action = 'sell'
else:
    action = 'hold'
print(action)

#and / or
mo = True
if mo and sp >=150:
    action = 'sell'
if not mo or sp < 140:
    action = 'buy'
print(action)

#nested
if not mo:
    if sp > 160:
        action = 'sell'
print(action)