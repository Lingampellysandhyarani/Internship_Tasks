Problem 10 : CamelCase
HackerRank : https://www.hackerrank.com/challenges/camelcase/problem


def camelcase(s):
    count = 1

    for ch in s:
        if ch.isupper():
            count += 1

    return count


s = input()
print(camelcase(s))
