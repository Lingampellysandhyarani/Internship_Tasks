Problem 14 :Anagram
HackerRank : https://www.hackerrank.com/challenges/anagram/problem

from collections import Counter

def anagram(s):
    if len(s) % 2 != 0:
        return -1

    mid = len(s) // 2
    s1 = s[:mid]
    s2 = s[mid:]

    count1 = Counter(s1)
    count2 = Counter(s2)

    changes = 0

    for ch in count1:
        if count1[ch] > count2[ch]:
            changes += count1[ch] - count2[ch]

    return changes


q = int(input())

for _ in range(q):
    s = input()
    print(anagram(s))
