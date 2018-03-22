#!/bin/python3

import sys

def timeConversion(s):
    ampm = s[-2:]
    t = s[:-2].split(':')
    if t[0] == '12': t[0] = '00'
    if ampm == 'PM': t[0] = str(int(t[0]) + 12)
    return ':'.join(t)

s = input().strip()
result = timeConversion(s)
print(result)
