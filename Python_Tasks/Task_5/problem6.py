Problem 6  : Introduction to sets
HackerRank : https://www.hackerrank.com/challenges/py-introduction-to-sets/problem

def average(array):

    distinct = set(array)
    avg = sum(distinct) / len(distinct)
    return round(avg, 3)


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
