#!/bin/python3

import sys

def breakingRecords(score):
    f = score.pop(0)
    highest, lowest = f, f
    ch, cl = 0, 0

    for s in score:
        if s > highest:
            # print("score {} is new highest, {}".format(s, ch))
            highest = s
            ch += 1
        if s < lowest:
            # print("score {} is new lowest, {}".format(s, cl))
            lowest = s
            cl += 1
    return [ch, cl]

if __name__ == "__main__":
    n = int(input().strip())
    score = list(map(int, input().strip().split(' ')))
    result = breakingRecords(score)
    print (" ".join(map(str, result)))


