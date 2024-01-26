import time
import functools
import sys

def read_vault(file_path):
    with open(file_path, 'r') as file:
        vault = [list(map(int, line.split(','))) for line in file]
    return vault

@functools.lru_cache(maxsize=50000) 
def find_max_coins(vault, row, col):
    if row == 0 and col == 0:
        return vault[row][col], ''
    if row < 0 or col < 0: 
        return 0, ''
    north_coins, north_path = find_max_coins(vault, row - 1, col)
    west_coins, west_path = find_max_coins(vault, row, col - 1)
    if north_coins > west_coins:
        return north_coins + vault[row][col], 'N' + north_path
    else:
        return west_coins + vault[row][col], 'W' + west_path

if __name__ == '__main__':
    vault = read_vault(sys.argv[1])
    start_time = time.perf_counter_ns()
    total_coins, path = find_max_coins(tuple(map(tuple, vault)), len(vault) - 1, len(vault[0]) - 1)
    end_time = time.perf_counter_ns()
    print(path[::-1]) 
    print(total_coins)
    print(end_time - start_time)
