Problem 3  : Mars Exploration
HackerRank : https://www.hackerrank.com/challenges/mars-exploration/problem


def marsExploration(s):
    changes = 0

    for i in range(len(s)):
        if s[i] != "SOS"[i % 3]:
            changes += 1

    return changes

s = input()
print(marsExploration(s))
