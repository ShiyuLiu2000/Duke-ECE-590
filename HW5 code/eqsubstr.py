# Write a function, which when iven one string (s) and two characters
# (c1 and c2), computes all pairings of contiguous ranges of c1s
# and c2s that have the same length.  Your function should return
# a set of three-tuples.  Each element of the set should be
# (c1 start index, c2 start index, length)
#
# Note that s may contain other characters besides c1 and c2.
# Example:
#  s = abcabbaacabaabbbb
#      01234567890111111  <- indices for ease of looking
#                1123456
#  c1 = a
#  c2 = b
#  Observe that there are the following contiguous ranges of 'a's (c1)
#  Length 1: starting at 0, 3, 9
#  Length 2: starting at 6, 11
#  And the following contiguous ranges of 'b's (c2)
#  Length 1: starting at 1, 10
#  Length 2: starting at 4
#  Length 4: starting at 13
#  So the answer would be
#  { (0, 1, 1), (0, 10, 1), (3, 1, 1), (3, 10, 1), (9, 1, 1), (9, 10, 1),
#    (6, 4, 2), (11, 4, 2)}
#  Note that the length 4 range of 'b's does not appear as there are no
#  Length 4 runs of 'a's.

def matching_length_sub_strs(s, c1, c2):
    def find_sequences(s, c):
        i = 0
        while i < len(s):
            if s[i] == c:
                start = i
                while i < len(s) and s[i] == c:
                    i += 1
                yield (start, i - start)
            i += 1
    matches = set()
    c1_sequences = list(find_sequences(s, c1))
    c2_sequences = list(find_sequences(s, c2))
    for c1_start, c1_length in c1_sequences:
        for c2_start, c2_length in c2_sequences:
            if c1_length == c2_length:
                matches.add((c1_start, c2_start, c1_length))
    return matches


# Makes a random string of length n
# The string is mostly comprised of 'a' and 'b'
# So you should use c1='a' and c2='b' when
# you use this with matching_length_sub_strs
def rndstr(n):
    def rndchr():
        x=random.randrange(7)
        if x==0:
            return chr(random.randrange(26)+ord('A'))
        if x<=3:
            return 'a'
        return 'b'
    ans=[rndchr() for i in range(n)]
    return "".join(ans)

    
import random
import time
import math

def generateData(N):
    return rndstr(N)

def getRuntime(s, c1, c2):
    start = time.perf_counter()
    result = matching_length_sub_strs(s, c1, c2)
    end = time.perf_counter()
    return 1000 * (end - start), result

if __name__ == "__main__":
    sizes = [2 ** i for i in range(9, 15)]
    c1 = 'a'
    c2 = 'b'

    compare_base = getRuntime(generateData(sizes[0]), c1, c2)[0]

    for size in sizes:
        s = generateData(size)
        runtime, results = getRuntime(s, c1, c2)
        log = math.log2(runtime / compare_base)
        runtime = round(runtime)
        log = round(log)
        ans = [size, runtime, log]
        print(ans)
