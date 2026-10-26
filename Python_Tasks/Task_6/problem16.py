Problem 16 : Check subset
HackerRank : https://www.hackerrank.com/challenges/py-check-subset/problem

t = int(input())

for _ in range(t):
    a = int(input())
    A = set(map(int, input().split()))

    b = int(input())
    B = set(map(int, input().split()))

    print(A.issubset(B))
