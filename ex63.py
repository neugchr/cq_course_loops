from random import randint
from random import seed

seed(123)

l = []
for i in range(1,randint(21,31)):
    l.append(randint(1,1000))
print(l)
total = 0
for i in l:
    total += i
print(total)

comp = int(input('compare contents to what number: '))
for i in l:
    if i > comp:
        print('bigger')
    elif i < comp:
        print('smaller')
    elif i == comp:
        print('equal')
    else:
        print('oh noes this should have been impossible')
