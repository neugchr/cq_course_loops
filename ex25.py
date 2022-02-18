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

def show(mtrx):
    x=0
    y=0
    ostr = ''
    while y < len(mtrx):
        while x < len(mtrx[y]):
            ostr += str(mtrx[y][x])+'\t'
            x+=1
        ostr+='\n'
        x=0
        y+=1
    return(ostr)

print(show(matrix))
print(show(matrix2))
print(show(matrix3))


def matrixmultiplication(m1,m2):
    m1_xdim = len(m1)
    m1_ydim = len(m1[0])
    m2_xdim = len(m2)
    m2_ydim = len(m2[0])

    outmatrix = []
    om_xdim = m2_xdim
    om_ydim = m1_ydim
    for x in range(om_xdim):
        tmp = []
        for y in range(om_ydim):
            tmp.append('None')
        outmatrix.append(tmp)


    for col in m1:
        if len(col) != m1_ydim:
            print('matrix 1 column lenght not uniform')
            return(None)
    for col in m2:
        if len(col) != m2_ydim:
            print('matrix 2 column lenght not uniform')
            return(None)

    if m1_xdim != m2_ydim:
        print('matrices can not be multiplied')
        return(None)
    # multiply every x position of matrix 1
    # with the corresponding y position of matrix 2
    # and store it in the resultmatrix at position (col_2=x, row_1=y)
    for ox in range(om_xdim):
        for oy in range(om_ydim):
            for x in range(m1_xdim):
                for y in range(m2_ydim):
                    outmatrix[ox][oy] = m1[x][oy] * m2[ox][y]
    return(outmatrix)


matrixm1 = []
for i in range(3):
    tmp = []
    for j in range(6):
        tmp.append(randint(1,10))
    matrixm1.append(tmp.copy())
print('this is m1', matrixm1)

matrixm2 = []
for i in range(4):
    tmp = []
    for j in range(3):
        tmp.append(randint(-2,2))
    matrixm2.append(tmp.copy())

print("multiply matrix 1")
print(show(matrixm1))
print('with matrix 2')
print(show(matrixm2))
matrixm3 = matrixmultiplication(matrixm1, matrixm2)
print('result is')
print(show(matrixm3))
