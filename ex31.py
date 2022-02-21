from random import randint
from random import shuffle
import time

def all_the_stuff(i, j):
    return(i+j, i-j, i*j, i/j)


for i in range(3):
    r1 = randint(-20,20)
    r2 = randint(-20,20)
    rslt = all_the_stuff(r1,r2)
    print('addition of', r1, 'and', r2, 'yields:', rslt[0])
    print('subtraction of', r2, 'from', r1, 'yields:', rslt[1])
    print('multiplication of', r1, 'and', r2, 'yields:', rslt[2])
    print('division of', r1, 'by', r2, 'yields:', rslt[3])
    print('\n')


print('onto exercise 31\n')

def sumlistandinvert(inputlist):
    accum = 0
    outlist = []
    for i in range(len(inputlist)):
        outlist.insert(0, inputlist[i])
        accum += inputlist[i]
    return(outlist, accum)
res = sumlistandinvert([1,2,3,4,5])
print(res[0])
print(res[1])
