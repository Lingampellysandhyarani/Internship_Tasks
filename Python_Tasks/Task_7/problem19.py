Problem 19 : Weighted Uniform Strings
HackerRank : https://www.hackerrank.com/challenges/weighted-uniform-string/problem

import math
import os
import random
import re
import sys

def weightedUniformStrings(s, queries):
    weights = set()
    previous = ""
    current_weight = 0

    for ch in s:
        weight = ord(ch) - ord('a') + 1

        if ch == previous:
            current_weight += weight
        else:
            current_weight = weight

        weights.add(current_weight)
        previous = ch

    return ["Yes" if q in weights else "No" for q in queries]

s = input().strip()
n = int(input())

queries = []
for _ in range(n):
    queries.append(int(input()))

result = weightedUniformStrings(s, queries)
print("\n".join(result))
