# Problem 10  : Find a string
# HackerRank  : https://www.hackerrank.com/challenges/find-a-string/problem

def count_substring(string, sub_string):
    count = 0
    a = len(string)
    b = len(sub_string)
    
    for i in range(a):
        if string[i:i+b] == sub_string:
            count = count + 1
            
    return count
if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
