Problem  6 : pangrams
HackerRank : https://www.hackerrank.com/challenges/pangrams/problem

def pangrams(s):
    letters = set(s.lower())
    return "pangram" if len(letters & set("abcdefghijklmnopqrstuvwxyz")) == 26 else "not pangram"

print(pangrams(input()))
