#!/bin/python3

import sys

def plusMinus(arr):
    o1 = 0
    o2 = 0
    o3 = 0
    l = len(arr)
    for x in range(0,l):
        if arr[x] > 0: o1 += 1
        elif arr[x] < 0: o2 += 1
        else: o3 += 1
    try:
        print( format(1/(l/o1), '.6f') )
    except ZeroDivisionError:
        print( format(0, '.6f') )
    try:
        print( format(1/(l/o2), '.6f') )
    except ZeroDivisionError:
        print( format(0, '.6f') )
    try:
        print( format(1/(l/o3), '.6f') )
    except ZeroDivisionError:
        print( format(0, '.6f') )


if __name__ == "__main__":
    n = int(input().strip())
    arr = list(map(int, input().strip().split(' ')))
    plusMinus(arr)
