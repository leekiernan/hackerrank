#!/bin/python3

import sys

def miniMaxSum(arr):
    min = sum(arr)
    max = 0
    for x in range(0,len(arr)):
        new_arr = arr[:]
        del new_arr[x]
        s = sum(new_arr)
        if s < min: min = s
        if s > max: max = s

    print( "{0} {1}".format(min, max) )

if __name__ == "__main__":
    arr = list(map(int, input().strip().split(' ')))
    miniMaxSum(arr)
