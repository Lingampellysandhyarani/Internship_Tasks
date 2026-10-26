Problem 20 : Validating phone numbers
HackerRank : https://www.hackerrank.com/challenges/validating-the-phone-number/problem?utm_source=chatgpt.com

import re

for _ in range(int(input())):
    number = input()

    if re.match(r'^[789]\d{9}$', number):
        print("YES")
    else:
        print("NO")
