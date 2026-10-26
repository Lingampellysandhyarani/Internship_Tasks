Problem 17 : Separate The numbers
HackerRank : https://www.hackerrank.com/challenges/separate-the-numbers/problem


def separateNumbers(s):
    n = len(s)

    for length in range(1, n // 2 + 1):
        first = s[:length]

        if first.startswith('0'):
            continue

        num = int(first)
        expected = first

        while len(expected) < n:
            num += 1
            expected += str(num)

        if expected == s:
            print("YES", first)
            return

    print("NO")


q = int(input())

for _ in range(q):
    s = input().strip()
    separateNumbers(s)
