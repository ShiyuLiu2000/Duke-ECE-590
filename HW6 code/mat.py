import time
import functools
import sys

def read_matrices(file_path):
    with open(file_path, 'r') as file:
        matrices = [(line.split(',')[0], int(line.split(',')[1]), int(line.split(',')[2])) for line in file.readlines()]
    return matrices

@functools.lru_cache(maxsize=1000000)
def matrix_chain_order(p, i, j):
    if i == j:
        return 0
    min_ops = float('inf')
    k_best = None
    for k in range(i, j):
        ops_left = matrix_chain_order(p, i, k)
        ops_right = matrix_chain_order(p, k + 1, j)
        ops_mult = p[i][1] * p[k][2] * p[j][2]
        total_ops = ops_left + ops_right + ops_mult
        if total_ops < min_ops:
            min_ops = total_ops
            k_best = k
    return min_ops

def construct_optimal_solution(p, i, j):
    if i == j:
        return p[i][0]
    for k in range(i, j):
        if matrix_chain_order(p, i, k) + matrix_chain_order(p, k + 1, j) + p[i][1] * p[k][2] * p[j][2] == matrix_chain_order(p, i, j):
            return (construct_optimal_solution(p, i, k), construct_optimal_solution(p, k + 1, j))
    return None

if __name__ == '__main__':
    matrices = read_matrices(sys.argv[1])
    start_time = time.perf_counter_ns()
    p = tuple((name, rows, cols) for name, rows, cols in matrices)
    min_ops = matrix_chain_order(p, 0, len(p) - 1)
    optimal_solution = construct_optimal_solution(p, 0, len(p) - 1)
    end_time = time.perf_counter_ns()
    print(optimal_solution)
    print(min_ops)
    print(end_time - start_time)
