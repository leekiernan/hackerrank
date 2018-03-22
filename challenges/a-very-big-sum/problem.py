#!/bin/python3

import sys

def aVeryBigSum(n, ar):
    total = 0
    for x in range(0,n):
        total += ar[x]
    return total

n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = aVeryBigSum(n, ar)
print(result)
