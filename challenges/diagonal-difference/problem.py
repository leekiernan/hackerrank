#!/bin/python3

import sys

def diagonalDifference(a):
    l = len(a[0])
    c1 = 0
    c2 = 0
    for x in range(0,l):
        c1 += a[x][x]
        c2 += a[x][l-1-x]
    return abs(c2-c1)

if __name__ == "__main__":
    n = int(input().strip())
    a = []
    for a_i in range(n):
       a_t = [int(a_temp) for a_temp in input().strip().split(' ')]
       a.append(a_t)
    result = diagonalDifference(a)
    print(result)
