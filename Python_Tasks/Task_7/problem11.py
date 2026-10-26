Problem 11 :Two Strings
HackerRank : https://www.hackerrank.com/challenges/two-strings/problem

import math
import os
import random
import re
import sys


def twoStrings(s1, s2):
    if set(s1) & set(s2):
        return "YES"
    else:
        return "NO"


p = int(input())

for _ in range(p):
    s1 = input()
    s2 = input()
    print(twoStrings(s1, s2))
