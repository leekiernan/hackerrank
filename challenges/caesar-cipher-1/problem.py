#!/bin/python3

import sys

def changeLetter(s, k):
	alpha = list("abcdefghijklmnopqrstuvwxyz")

	try:
		up = s.isupper()
		cur = alpha.index(s.lower())
		new_pos = (cur + k) % len(alpha)
		return alpha[new_pos].upper() if up else alpha[new_pos]
	except ValueError:
		return s

def caesarCipher(s, k):
	return ''.join(list(map( lambda x: changeLetter(x, k), s)))

if __name__ == "__main__":
    n = int(input().strip())
    s = input().strip()
    k = int(input().strip())
    result = caesarCipher(s, k)
    print(result)
