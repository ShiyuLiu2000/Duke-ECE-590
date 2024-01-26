# removes duplicates from data.
# This function keeps the last occurence of each element
# and preserves order.
# So rmdup([1,2,3,2,1,4,2]) should return [3,1,4,2]
def rmdup(data):
    my_dict = {}
    for i in range(len(data)):
        my_dict[data[i]] = i
    res = []
    seen = set()
    for i in range(len(data)):
        if i == my_dict[data[i]] and data[i] not in seen:
            seen.add(data[i])
            res.append(data[i])
    return res

# print(rmdup([1,2,3,2,1,4,2]))

import random
import time
import math

def generateData(size, mode):
    # many duplicates
    if mode == 1: 
        return [random.randrange(0, size // 2048) for _ in range(size)]
    # moderate duplicates
    if mode == 2:
        return [random.randrange(0, size // 16) for _ in range(size)]
    # rare duplication
    if mode == 3:
        return [random.randrange(0, size * 4) for _ in range(size)]

def getRuntime(size, mode):
    data = generateData(size, mode)
    start = time.perf_counter()
    new_data = rmdup(data)
    end = time.perf_counter()
    return 1000 * (end - start)

# run tests
if __name__ == "__main__":
    sizes = [2 ** i for i in range(12, 23)] # from 4K(2^12) to 4M(2^23)

    compare_base = [getRuntime(sizes[0], i) for i in range(1, 4)]
    
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
