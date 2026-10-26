Problem 13 : Sherlock and the Valid String
HackerRank : https://www.hackerrank.com/challenges/sherlock-and-valid-string/problem


import math
import os
import random
import re
import sys


from collections import Counter

def isValid(s):
    char_freq = Counter(s)
    freq_counts = Counter(char_freq.values())

    if len(freq_counts) == 1:
        return "YES"

    if len(freq_counts) > 2:
        return "NO"

    (f1, c1), (f2, c2) = freq_counts.items()

    # One character occurs once and can be removed
    if (f1 == 1 and c1 == 1) or (f2 == 1 and c2 == 1):
        return "YES"

    # One character occurs one extra time
    if abs(f1 - f2) == 1:
        if (f1 > f2 and c1 == 1) or (f2 > f1 and c2 == 1):
            return "YES"

    return "NO"


s = input()
print(isValid(s))
