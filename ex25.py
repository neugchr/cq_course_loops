from random import randint

matrix = []
for i in range(3):
    tmp = []
    for j in range(5):
        tmp.append(randint(10,100))
    matrix.append(tmp.copy())

print(matrix)

max = 0
pos = (0,0)
sum = 0
for o in range(len(matrix)):
    for i in range(len(matrix[o])):
        if matrix[o][i] > max:
            max = matrix[o][i]
            pos = (o,i)
        sum += matrix[o][i]

print('max of', max, 'at', pos)
print('sum is:', sum)


matrix2 = []
matrix3 = []
for sub in matrix:
    tmp = []
    tmp2 = []
    for elem in sub:
        tmp.append(randint(-5,6))
        tmp2.append(None)
    matrix2.append(tmp.copy())
    matrix3.append(tmp2.copy())

print(matrix2)

for x in range(len(matrix)):
    for y in range(len(matrix[x])):
        matrix3[x][y] = matrix[x][y]*matrix2[x][y]

print(matrix3)
