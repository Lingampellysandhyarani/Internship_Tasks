Problem 16 : Caesar Cipher
HackerRank : https://www.hackerrank.com/challenges/caesar-cipher-1/problem

import math
import os
import random
import re
import sys

def caesarCipher(s, k):
    result = ""
    k = k % 26

    for ch in s:
        if ch.islower():
            result += chr((ord(ch) - ord('a') + k) % 26 + ord('a'))
        elif ch.isupper():
            result += chr((ord(ch) - ord('A') + k) % 26 + ord('A'))
        else:
            result += ch

    return result
n = int(input())
s = input()
k = int(input())

print(caesarCipher(s, k))
