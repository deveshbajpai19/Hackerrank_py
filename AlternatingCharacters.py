__author__ = 'deveshbajpai'
'''
Problem Url: https://www.hackerrank.com/challenges/alternating-characters

Algorithm: Run a loop over the string's length till the last but one character. Check if the current character is same
as the next character and increment the count if yes. After the string iteration, return the count as the final answer.
'''
def solve(s):
    count = 0
    for i in xrange(0,len(s)-1,1):
        if s[i]==s[i+1]:
            count+=1
    return count



if __name__ == "__main__":
    cases = int(input())
    results = []
    for case in range(cases):
        results.append(solve(raw_input().lower()))
    for result in results:
        print result