import random
import sys
import math
import time

# from tqdm import tqdm

random.seed(0)

# placeholder for now
best_crossover_point = 60

# placeholder for size of matrix for trianglization
const = 1024

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
            bruh.append(int(lines[i * n + j]))
        A.append(bruh)

    m = n*n
    for i in range(n):
        bruh = []
        for j in range(n):
            bruh.append(int(lines[i * n + j + m]))
        B.append(bruh)

    return A, B


def findDiagonals(matrix):
    diagonals = []
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if i == j:
                diagonals.append(matrix[i][j])
    return diagonals


# regular matrix multiplication
def standardProduct(A, B):
    n = len(A)
    C = [[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                C[i][j] += A[i][k] * B[k][j]
    return C


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

# pads matrix A and B with a row and col of 0s, returning modified versions


def pad(A, B):
    row0 = [0 for i in range(0, len(A) + 1)]
    for i in range(len(A)):
        A[i].append(0)
        B[i].append(0)
    A.append(row0)
    B.append(row0)


def strassen(A, B, cross):
    if len(A) <= cross and len(A[0]) <= cross:
        return standardProduct(A, B)

    # pads the matrix with 0s if odd
    odd = False
    if len(A) % 2 != 0 or len(A[0]) % 2 != 0:
        odd = True
        pad(A, B)

    a1, a2, a3, a4 = splitMatrix(A)
    b1, b2, b3, b4 = splitMatrix(B)

    p1 = strassen(a1, subtract(b2, b4), cross)
    p2 = strassen(add(a1, a2), b4, cross)
    p3 = strassen(add(a3, a4), b1, cross)
    p4 = strassen(a4, subtract(b3, b1), cross)
    p5 = strassen(add(a1, a4), add(b1, b4), cross)
    p6 = strassen(subtract(a2, a4), add(b3, b4), cross)
    p7 = strassen(subtract(a1, a3), add(b1, b2), cross)

    tl = add(subtract(add(p5, p4), p2), p6)
    tr = add(p1, p2)
    bl = add(p3, p4)
    br = subtract(subtract(add(p1, p5), p3), p7)

    # construct the new matrix from our 4 quadrants
    new_matrix = []
    for i in range(len(tr)):
        new_matrix.append(tl[i] + tr[i])
    for i in range(len(br)):
        new_matrix.append(bl[i] + br[i])

    # pop off 0s if necessary (maybe combining this w/ above will be more efficient)
    if odd == True:
        for i in range(len(new_matrix)):
            A[i].pop()
            B[i].pop()
            new_matrix[i].pop()
        new_matrix.pop()
        A.pop()
        B.pop()

    return new_matrix

# task number 3


def createAdjMatrix(p):
    # const is defined at top of file, final value to be 1024
    half_const = int(const / 2)
    AdjMatrix = [[0 for j in range(const)] for i in range(const)]
    for i in range(const):
        for j in range(half_const):
            # doesn't count a path from a node to itself
            if i != j:
                if random.randint(1, 101) <= p:
                    AdjMatrix[i][j] = AdjMatrix[j][i] = 1

    return AdjMatrix


def findTriangles(A):
    # can use strassen too if it's faster, using the global variable
    # "best_crossover_point" as the cross parameter
    B = standardProduct(A, A)
    B = standardProduct(B, A)
    diagonals = findDiagonals(B)
    sum = 0
    triangles = 0
    for diagonal in diagonals:
        sum += diagonal

    triangles = sum / 6

    return int(triangles)


if __name__ == "__main__":

    # standard crossing point for strassen
    cross = 60
    n = 0
    optimize = False
    trials = 1
    ft = False
    p = 5

    if len(sys.argv) != 3 and len(sys.argv) != 4:
        print("Proper usage: python strassen.py {0} {dimension} {input file}")
        sys.exit()

    for i, arg in enumerate(sys.argv):
        if i == 1:
            # if it's 0, don't optimize
            if int(arg) > 0:
                optimize = True
                trials = int(arg)
            elif int(arg) == 0:
                ft = True
        if i == 2:
            n = int(arg)

            # for our testing purposes, delete when turning into gradescope
            A, B = createRandomMatrices(int(arg))
            writeMatrix(A, B, str(arg)+"d.in")
        if i == 3:
            A, B = read(arg)
            start = int(round(time.time() * 100000))
            C = standardProduct(A, B)
            end = int(round(time.time() * 100000))
            std = end - start
            for diagonal in findDiagonals(C):
                print(diagonal)
            print()
            print("standard matrix multiplication: " +
                  str(std) + " microseconds")

            start = int(round(time.time() * 100000))
            D = strassen(A, B, cross)
            end = int(round(time.time() * 100000))
            for diagonal in findDiagonals(D):
                print(diagonal)
            print()
            print("strassen's multiplication: " +
                  str(end - start) + " microseconds")
            strassenTime = end - start

            if ft == True:
                A = createAdjMatrix(p)
                n_triangles = findTriangles(A)
                print("number of triangles, matrix of size " + str(const) +
                      " with p = " + str(p) + ": " + str(n_triangles))

            if optimize == True:
                for j in range(trials):
                    min = (2, float('inf'))
                    for k in range(30):
                        start = int(round(time.time() * 100000))
                        D = strassen(A, B, k + 50)
                        end = int(round(time.time() * 100000))
                        if (end - start) < min[1]:
                            min = (k + 50, end - start)
                    print("optimized strassen's (cross = " +
                          str(min[0]) + "): " + str(min[1]) + " microseconds")
            else:
                print("strassen's multiplication: " +
                      str(end - start) + " microseconds")
                strassenTime = end - start
