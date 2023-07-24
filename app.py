import random

def printMatrix (matrix):    
    for i in matrix:
        print(*i)


def generateMat (rows, cols):
    matrix = []
    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(random.randint(0, 9))
        matrix.append(row)
    return matrix
rows = int(input("input rows "))
cols = int(input("input columns "))


def addMatrix (matrix1, matrix2):
    result = []
    printMatrix(matrix1)
    print("add to")
    printMatrix(matrix2)

    for i, col1 in enumerate(matrix1):
        resultRow = []
        for j, val in enumerate(col1):
            resultRow.append(val + matrix2[i][j])  
        result.append(resultRow)
    print("result")
    printMatrix(result)


matrix1 =  generateMat(rows, cols)
matrix2 = generateMat(rows, cols)

addMatrix(matrix1, matrix2)