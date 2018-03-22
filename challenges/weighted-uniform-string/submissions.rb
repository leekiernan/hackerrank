#!/bin/python3

import sys

s = input().strip()
n = int(input().strip())

ar = dict()
pr = ''
w = 0
for i in range(len(s)):
    if s[i] != pr: w = 0
    w += ord(s[i]) - 96
    ar[w] = True
    pr = s[i]



for a0 in range(n):
    x = int(input().strip())
    print("Yes") if x in ar else print("No")
