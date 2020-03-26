import random
import sys
import math
import time

random.seed(32)


# creating and writing the test matrices to a file
def createRandomMatrices(n):
    max = 4
    matrix1 = []
    matrix2 = []
    for i in range(n):
        matrix1.append([random.randint(0, max) for j in range(n)])
    for i in range(n):
        matrix2.append([random.randint(0, max) for j in range(n)])

    return matrix1, matrix2


def writeMatrix(A, B, fName):
    f = open(fName, 'w')
    for line in A:
        for char in line:
            if char != " ":
                f.write(str(char) + "\n")
    for line in B:
        for char in line:
            if char != " ":
                f.write(str(char) + "\n")


# writes to a file named "{DIMENSION}d.in"
n = 4
A, B = createRandomMatrices(n)
writeMatrix(A, B, str(n)+"d.in")


# reading test matrices from a file
def read(fName):
    lines = open(fName, 'r').read().splitlines()
    two_n_squared = len(lines)
    n = int(math.sqrt(two_n_squared / 2))
    A = []
    B = []
    for i in range(n):
        bruh = []
        for j in range(n):
            bruh.append(int(lines[i * j + j]))
        A.append(bruh)

    const = n*n
    for i in range(n):
        bruh = []
        for j in range(n):
            bruh.append(int(lines[i * j + j + const]))
        B.append(bruh)

    return A, B


def printDiagonals(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if i == j:
                print("(" + i + ", " + j + "): " + {matrix[i][j]})


# regular matrix multiplication
def standardProduct(A, B):
    n = len(A)
    C = [[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                C[i][j] += A[i][k] * B[k][j]
    printDiagonals(C)


# addition and subtraction functions for strassen
def add(A, B):
    n = len(A)
    C = [[0 for j in range(0, n)] for i in range(0, n)]
    for i in range(0, n):
        for j in range(0, n):
            C[i][j] = A[i][j] + B[i][j]
    return C


def subtract(A, B):
    n = len(A)
    C = [[0 for j in range(0, n)] for i in range(0, n)]
    for i in range(0, n):
        for j in range(0, n):
            C[i][j] = A[i][j] - B[i][j]
    return C

# split matrix for strassen


def splitMatrix(A):

    if len(A) % 2 != 0 or len(A[0]) % 2 != 0:
        raise Exception('Odd matrices are not supported!')

    matrixLen = len(A)
    midPoint = matrixLen // 2
    tl = [[A[i][j] for j in range(midPoint)] for i in range(midPoint)]
    bl = [[A[i][j] for j in range(midPoint)]
          for i in range(midPoint, matrixLen)]

    tr = [[A[i][j] for j in range(midPoint, matrixLen)]
          for i in range(midPoint)]
    br = [[A[i][j] for j in range(midPoint, matrixLen)]
          for i in range(midPoint, matrixLen)]

    return tl, tr, bl, br


def strassen(A1, B1):
    if len(A1) == 2 and len(A1[0]) == 2:
        return standardProduct(A1, B1)

    A, B, C, D = splitMatrix(A1)
    E, F, G, H = splitMatrix(B1)
    print(A)

    p1 = strassen(A, subtract(F, H))
    p2 = strassen(add(A, B), H)
    p3 = strassen(add(C, D), E)
    p4 = strassen(D, subtract(G, E))
    p5 = strassen(add(A, D), add(E, H))
    p6 = strassen(subtract(B, D), add(G, H))
    p7 = strassen(subtract(A, C), add(E, F))

    tl = add(subtract(add(p5, p4), p2), p6)
    tr = add(p1, p2)
    bl = add(p3, p4)
    br = subtract(subtract(add(p1, p5), p3), p7)

    # construct the new matrix from our 4 quadrants
    new_matrix = []
    for i in range(len(top_right)):
        new_matrix.append(top_left[i] + top_right[i])
    for i in range(len(bot_right)):
        new_matrix.append(bot_left[i] + bot_right[i])
    return new_matrix


if __name__ == "__main__":

    n = 0

    if len(sys.argv) != 3 and len(sys.argv) != 4:
        print("Proper usage: python strassen.py {0} {dimension} {input file}")
        sys.exit()

    for i, arg in enumerate(sys.argv):
        if i == 0:
            print("first argument has not been altered to do anything")
        if i == 2:
            n = int(arg)

            # for our testing purposes, delete when turning into gradescope
            A, B = createRandomMatrices(int(arg))
            writeMatrix(A, B, str(arg)+"d.in")
        if i == 3:
            A, B = read(arg)
            print("read")
            start = int(round(time.time() * 100000))
            standardProduct(A, B)
            end = int(round(time.time() * 100000))
            print("standard matrix multiplication: " +
                  str(end - start) + " microseconds")
            # start = int(round(time.time() * 100000))
            # strassen(A, B)
            # end = int(round(time.time() * 100000))
            # print("strassen method multiplication: " +
            #       str(end - start) + " microseconds")
