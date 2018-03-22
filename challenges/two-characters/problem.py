#!/bin/python3

import sys
import re

def getPairs(s):
    chars = list(set(s))
    pairs = []
    c = 0
    while c < len(chars):
        if c+1 is None: break
        cc = c+1
        while cc < len(chars):
            pairs.append([chars[c], chars[cc]])
            cc += 1
        c += 1

    return pairs

def removeAllButPair(s, pair):
  # re.sub('[^'+re.escape(''.join(pair))+']', '', s)
  p = re.escape(''.join(pair))
  ss = re.findall('(['+p+'])', s)
  return ''.join(ss)

def length_of_string(s):
	c = 1;
	while c < len(s):
		if s[c] == s[c-1]: return 0
		c += 1

	return len(s)

def twoCharaters(s):
    # Complete this function
    pairs = getPairs(s)
    longest = 0
    for p in pairs:
    	l = length_of_string(removeAllButPair(s, p))
    	if l > longest: longest = l
    return longest

if __name__ == "__main__":
    l = int(input().strip())
    s = input().strip()
    result = twoCharaters(s)
    print(result)
