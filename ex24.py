from random import randint
from random import seed

seed(123)

l = []
for i in range(1,randint(21,31)):
    l.append(randint(1,1000))
print(l)

inp = int(input('What number so scan for? '))
pos = 0
found = False
while pos < len(l):
    if l[pos] == inp:
        print("found", inp, "at position:", pos)
        found = True
    pos +=1
if not found:
    print(inp, "not found")


l = list(range(1,randint(5,10)))
o = 0
while o < len(l):
    i = 0
    while i < len(l):
        print(o,'*',i,'=',o*i)
        i +=1
    o +=1


l = ("Lorem ipsum dolor sit amet, consectetur adipisici elit, sed eiusmod tempor "
    +"incidunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis "
    +"nostrud exercitation ullamco laboris nisi ut aliquid ex ea commodi consequat. "
    +"Quis aute iure reprehenderit in voluptate velit esse cillum dolore eu fugiat "
    +"nulla pariatur. Excepteur sint obcaecat cupiditat non proident, sunt in culpa "
    +"qui officia deserunt mollit anim id est laborum.")
l = l.split()
l = l[0:randint(2,len(l))]

i = 0
while i < len(l):
    print(l[i])
    i +=1
