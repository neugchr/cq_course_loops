from random import randint
from random import shuffle
import time

def pls(i, j):
    return(i+j)

def mns(i,j):
    return(i-j)

def mlt(i,j):
    return(i*j)

def div(n,d):
    return(n/d)


for i in range(3):
    r1 = randint(-20,20)
    r2 = randint(-20,20)
    print('addition of', r1, 'and', r2, 'yields:', pls(r1,r2))
    print('subtraction of', r2, 'from', r1, 'yields:', mns(r1,r2))
    print('multiplication of', r1, 'and', r2, 'yields:', mlt(r1,r2))
    print('division of', r1, 'by', r2, 'yields:', div(r1,r2))
    print('\n')


print('onto exercise 29\n')

def sumlist(inputlist):
    accum = 0
    for i in inputlist:
        accum += i
    return(accum)

def inverter(inputlist):
    outlist = []
    for i in range(len(inputlist)):
        outlist.insert(0, inputlist[i])
    return(outlist)

def stupidinvert(inputlist):
    start_time = time.time()
    inverted = False
    mixedlist = inputlist.copy()
    while not inverted:
        print('trying to invert:')
        print(inputlist)
        r = randint(1,3)
        if r == 1:
            print("shaking the set up")
        elif r == 2:
            print("stirring vigorously")
        else:
            print("engeging the mixer")
        shuffle(mixedlist)
        print("how does it look?")
        print(mixedlist)
        inverted = True     # obviously shuffling the list must have inverted it
        for i in range(0,len(inputlist)):
            if inputlist[i] != mixedlist[-i]:
                print('bad it looks bad\n')
                inverted = False    # but if it hasn't we need to try again
                break               # as soon as we realize we failed we need not continue - so important to save computation time
    print('seems alright to me\n')
    print("sorting finished after %s seconds" % (time.time() - start_time))
    return(mixedlist)



lst = []
for i in range(3):
    lst.append(randint(0,9))
print('this is our list')
print(lst)
print('summing up list elements')
print(sumlist(lst))
print('\ninverting the list the smart way')
print(inverter(lst))

print('\nnow reordering by mixing the list up')
inv = stupidinvert(lst)
print(inv)
