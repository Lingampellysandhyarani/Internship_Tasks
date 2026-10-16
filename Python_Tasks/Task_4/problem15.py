# Problem 15 : Word Order
# HackerRank : https://www.hackerrank.com/challenges/word-order/problem

n =int(input())

d ={}

for i in range(n):
    word = input()
    d[word]=d.get(word,0)+1
    
print(len(d))
print(*d.values())   
