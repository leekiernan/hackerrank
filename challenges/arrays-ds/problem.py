#!/bin/python3

import os
import sys

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().rstrip().split()))
    rev = []
    while n > 0:
        rev.append(str(arr[n -1]))
        n -= 1
    print(" ".join(rev))
