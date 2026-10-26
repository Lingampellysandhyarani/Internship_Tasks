Problem 20 : Super Reducd String
HackerRank : https://www.hackerrank.com/challenges/reduced-string/problem

def superReducedString(s):
    stack = []

    for ch in s:
        if stack and stack[-1] == ch:
            stack.pop()
        else:
            stack.append(ch)

    result = ''.join(stack)

    return result if result else "Empty String"


s = input().strip()
print(superReducedString(s))
