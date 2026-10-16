# Problem 14 : Set .add()
# HackerRank : https://www.hackerrank.com/challenges/py-set-add/problem


N = int(input())
s = set()
for i in range(N):
    s.add(input().strip())
print(len(s))
