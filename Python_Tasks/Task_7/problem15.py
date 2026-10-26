Problem 15 : Game of Thrones
HackerRank : https://www.hackerrank.com/challenges/game-of-thrones/problem

import math
import os
import random
import re
import sys


from collections import Counter

def gameOfThrones(s):
    freq = Counter(s)
    odd_count = sum(1 for count in freq.values() if count % 2 != 0)

    return "YES" if odd_count <= 1 else "NO"


if __name__ == '__main__':
    s = input().strip()
    print(gameOfThrones(s))
