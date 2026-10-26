Problem 15 : Set .difference() Operation
HackerRank : https://www.hackerrank.com/challenges/py-set-difference-operation/problem

n = int(input())
english = set(input().split())

m = int(input())
french = set(input().split())

print(len(english.difference(french)))
