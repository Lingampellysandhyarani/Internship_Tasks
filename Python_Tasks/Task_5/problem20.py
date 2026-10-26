Problem 20 : pilling Up!
HackerRank : https://www.hackerrank.com/challenges/piling-up/problem

from collections import deque

t = int(input())

for _ in range(t):
    n = int(input())
    cubes = deque(map(int, input().split()))

    last = float('inf')
    possible = True

    while cubes:
        if cubes[0] >= cubes[-1]:
            current = cubes.popleft()
        else:
            current = cubes.pop()

        if current > last:
            possible = False
            break

        last = current

    print("Yes" if possible else "No")
