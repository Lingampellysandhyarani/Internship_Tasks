Problem 19 : Merge_the_tools
HackerRank : https://www.hackerrank.com/challenges/merge-the-tools/problem

def merge_the_tools(string, k):
    for i in range(0, len(string), k):
        substring = string[i:i+k]

        unique = ""
        for ch in substring:
            if ch not in unique:
                unique += ch

        print(unique)

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
