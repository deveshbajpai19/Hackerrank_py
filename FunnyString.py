__author__ = 'deveshbajpai'

'''
Problem Url: https://www.hackerrank.com/challenges/funny-string

Algorithm: The solution is pretty much straightforward. The only improvement is avoid performing the reverse of the
string and take care of the difference of ASCII with help of indices. 
'''

def solve(str):
    l = str.__len__()
    i = 1
    j = l-1
    while(i<l-1 and j>0):
        val1 = abs(ord(str[i])-ord(str[i-1]))
        val2 = abs(ord(str[j-1])-ord(str[j]))
        if(val1 != val2):
            return "Not Funny"
        i+=1
        j-=1
    return "Funny"

if __name__ == "__main__":
    cases = int(input())
    results = []
    for case in range(cases):
        results.append(solve(raw_input()))
    for result in results:
        print result
