#!/bin/python3

import sys

def marsExploration(s):
    req = list("SOS")
    changed, x = 0, 0

    while x < len(s):
    	check = x % len(req)
    	# print("x {} ({}) check {} changed {}".format(x, s[x], check, s[x] != req[check]))
    	if s[x] != req[check]:
    		changed += 1
    	x += 1
    return changed

if __name__ == "__main__":
    s = input().strip()
    result = marsExploration(s)
    print(result)
