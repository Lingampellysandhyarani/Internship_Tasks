Problem 12 : Making Anagrams
HackerRank : https://www.hackerrank.com/challenges/making-anagrams/problem


def makingAnagrams(s1, s2):
    deletions = 0

    for ch in "abcdefghijklmnopqrstuvwxyz":
        deletions += abs(s1.count(ch) - s2.count(ch))

    return deletions


s1 = input()
s2 = input()

print(makingAnagrams(s1, s2))
