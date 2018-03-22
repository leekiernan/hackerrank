#!/bin/python3

import sys
from functools import reduce

def solve(n, s, d, m):
    count = 0
    for x in range(0,n):
        sl = s[x:x+m]
        # print("sum == {}".format(sum(sl)))
        if sum(sl) == d: count += 1

    return count

n = int(input().strip())
s = list(map(int, input().strip().split(' ')))
d, m = input().strip().split(' ')
d, m = [int(d), int(m)]
result = solve(n, s, d, m)
print(result)
