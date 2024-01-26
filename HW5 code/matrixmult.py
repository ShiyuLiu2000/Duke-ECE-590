# This function takes 2 matricies (as lists of lists)
# and performs matrix multiplication on them.
# Note: you may not use any matrix multiplication libraries.
# You need to do the multiplication yourself.
# For example, if you have
#     a=[[1,2,3],
#        [4,5,6],
#        [7,8,9],
#        [4,0,7]]
#     b=[[1,2],
#        [3,4],
#        [5,6]]
#  Then a has 4 rows and 3 columns.
#  b has 3 rows and 2 columns.
#  Multiplying a * b results in a 4 row, 2 column matrix:
#  [[22, 28],
#   [49, 64],
#   [76, 100],
#   [39, 50]]
def matrix_mul(a, b):
    numRows_a = len(a)
    numCols_a = len(a[0])
    numRows_b = len(b)
    numCols_b = len(b[0])
    ans = [[0 for i in range(numCols_b)] for j in range(numRows_a)]
    for row in range(numRows_a):
        for col_b in range(numCols_b):
            for col_a in range(numCols_a):
                ans[row][col_b] += a[row][col_a] * b[col_a][col_b]
    return ans

import random
import time
import math

def generateMatrix(N, mode):
    # many rows by few columns
    if mode == 1:
        a = [[random.randrange(100) for i in range(N)] for j in range(N // 4)]
        b = [[random.randrange(100) for i in range(N // 4)] for j in range(N)]
    # square
    elif mode == 2:
        a = [[random.randrange(100) for i in range(N)] for j in range(N)]
        b = [[random.randrange(100) for i in range(N)] for j in range(N)]
    # many columns by few rows
    elif mode == 3:
        a = [[random.randrange(100) for i in range(N // 4)] for j in range(N)]
        b = [[random.randrange(100) for i in range(N)] for j in range(N // 4)]
    return a, b

def getRuntime(N, mode):
    a, b = generateMatrix(N, mode)
    start = time.perf_counter()
    ans = matrix_mul(a, b)
    end = time.perf_counter()
    return 1000000 * (end - start)

if __name__ == "__main__":
    sizes = [2 ** i for i in range(2, 10)]

    compare_base = [getRuntime(sizes[0], i) for i in range(1, 4)]
    # print(compare_base)

    for size in sizes:
        times = []
        for i in range(1, 4):
            runtime = round(getRuntime(size, i))
            times.append(runtime)
        logs = []
        for i in range(3):
            log = math.log2(times[i] / compare_base[i])
            log = round(log)
            logs.append(log)
        ans = [size] + times + logs
        print(ans)
