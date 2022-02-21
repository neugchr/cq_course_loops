from random import randint


def creatematrix(columns, rows):
    mtrx = []
    for x in range(columns):
        tmp = []
        for y in range(rows):
            tmp.append(randint(-5,5))
        mtrx.append(tmp)
    return(mtrx)


def findmax(matrix):
    max = 0
    pos = (0,0)
    for col in range(len(matrix)):
        for row in range(len(matrix[col])):
            if matrix[col][row] > max:
                max = matrix[col][row]
                pos = (col,row)

    print('max of', max, 'at', pos)
    return (max, pos[0], pos[1])


def summatrix(matrix):
    sum = 0
    for col in range(len(matrix)):
        for row in range(len(matrix[col])):
            if matrix[col][row] > max:
                max = matrix[col][row]
                pos = (col,row)
            sum += matrix[col][row]
    print('sum is:', sum)
    return (sum)


def frmt(mtrx):
    col=0
    row=0
    ostr = ''
    while row < len(mtrx[0]):
        while col < len(mtrx):
            ostr += str(mtrx[col][row])+'\t'
            col +=1
        ostr+='\n'
        col=0
        row+=1
    return(ostr)


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

    if m1_xdim != m2_ydim:  # rows of matrix 1 needs to be of same length as columns of matrix 2
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



matrix_1 = creatematrix(3, 6)
matrix_2 = creatematrix(4, 3)
print(frmt(matrix_1))
print(findmax(matrix_1))
print(frmt(matrix_2))
print(findmax(matrix_2))


print("multiply matrix 1")
print(frmt(matrix_1))
print('with matrix 2')
print(frmt(matrix_2))
matrix_3 = matrixmultiplication(matrix_1, matrix_2)
print('result is')
print(frmt(matrix_3))
