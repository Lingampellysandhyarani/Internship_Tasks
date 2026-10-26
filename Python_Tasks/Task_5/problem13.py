Problem 13 : Nested Lists
HackerRank : https://www.hackerrank.com/challenges/nested-list/problem

if __name__ == '__main__':
    n = int(input())
records = []

for i in range(n):
    name = input()
    grade = float(input())
    records.append([name, grade])

grades = sorted(set([r[1] for r in records]))
second = grades[1]

names = []
for r in records:
    if r[1] == second:
        names.append(r[0])

names.sort()

for name in names:
    print(name)
