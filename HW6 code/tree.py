import time
import functools
import sys

class TreeNode:
    def __init__(self, val, freq, left=None, right=None):
        self.val = val
        self.freq = freq
        self.left = left
        self.right = right
        self.cost = None

    def __str__(self):
        if self.left is None and self.right is None:
            return str(self.val)
        left = str(self.left) if self.left is not None else '()'
        right = str(self.right) if self.right is not None else '()'
        return '({} {} {})'.format(self.val, left, right)
        
    def computeCost(self):
        if self.cost is not None:
            return self.cost
        def helper(n, depth):
            if n is None:
                return 0
            return depth * n.freq + helper(n.left, depth+1) + helper(n.right, depth +1)
        self.cost = helper(self, 1)
        return self.cost

def read_input(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    return [(int(line.split(':')[0]), int(line.split(':')[1])) for line in lines]

def construct_optimal_bst(keys, freqs):
    n = len(keys)
    cost = [[0 for _ in range(n)] for _ in range(n)]
    root = [[0 for _ in range(n)] for _ in range(n)]
    sum_freqs = [0] * (n + 1)
    for i in range(n):
        sum_freqs[i + 1] = sum_freqs[i] + freqs[i]
    for i in range(n):
        cost[i][i] = freqs[i]
        root[i][i] = i
    for L in range(2, n + 1):
        for i in range(n - L + 1):
            j = i + L - 1
            cost[i][j] = float('inf')
            for r in range(i, j + 1):
                c = (cost[i][r - 1] if r > i else 0) + (cost[r + 1][j] if r < j else 0) + sum_freqs[j+1] - sum_freqs[i]
                if c < cost[i][j]:
                    cost[i][j] = c
                    root[i][j] = r
    @functools.lru_cache(maxsize=1000000)
    def tree_from_root(i, j):
        if i > j:
            return None
        r = root[i][j]
        return TreeNode(keys[r], freqs[r], tree_from_root(i, r - 1), tree_from_root(r + 1, j))
    return tree_from_root(0, n - 1)

if __name__ == '__main__':
    items = read_input(sys.argv[1])
    keys, freqs = zip(*items)
    start_time = time.perf_counter_ns()
    root = construct_optimal_bst(keys, freqs)
    end_time = time.perf_counter_ns()
    print(root)
    print(root.computeCost())
    print(end_time - start_time)