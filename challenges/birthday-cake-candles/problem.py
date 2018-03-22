#!/bin/python3

import sys

def birthdayCakeCandles(n, ar):
    tallest = 0
    count = 0
    for x in range(0,n):
        if ar[x] > tallest: tallest = ar[x]

    for x in range(0,n):
        if ar[x] == tallest: count += 1

    return count

n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = birthdayCakeCandles(n, ar)
print(result)
