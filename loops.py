
sum = 0
for i in range(0,22):
    sum += i
print(sum)

sum = 0
for i in range(0,22):
    if i%2 == 0:
        sum += i
print(sum)

lst = []
for i in range(0,22):
    lst.insert(0, i)
print(lst)

sum = 0
for c in 'abcdefghijklmnopqrstuv':
    print(c)
    sum += ord(c)-97 # convert character into number and subtract offset
    print(sum)
print(sum)
