# Problem 19 : Collections.Counter()
# HackerRank : https://www.hackerrank.com/challenges/collections-counter/problem

from collections import Counter

X = int(input())
shoes = list(map(int, input().split()))

shoe_count = Counter(shoes)

N = int(input())
money = 0

for _ in range(N):
    size, price = map(int, input().split())

    if shoe_count[size] > 0:
        money += price
        shoe_count[size] -= 1

print(money)
