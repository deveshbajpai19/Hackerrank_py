__author__ = 'Devesh Bajpai'

'''
Problem Url: https://www.hackerrank.com/challenges/two-arrays

Algorithm: Sort one array in ascending and the other in descending order. This makes it possible to supply smallest
number for largest number to be just sufficient to be more than equal to k. Hence, run a loop over the arrays, and if
there is any encounter where the corresponding elements sum up to a value lesser than k, return NO. After the iteration,
return YES as all the arrays' elements have justified the condition.
'''

def solve(a,b,n,k):
    a.sort()
    b.sort(reverse=True)

    for i in xrange(0,n):
        if(a[i]+b[i]) < k:
            return "NO"

    return "YES"



if __name__ == "__main__":
    cases = int(input())
    results = []
    for case in range(cases):
        n,k = map(int,raw_input().split(" "))
        a = list()
        b = list()
        #input a and b lists
        a = map(int,raw_input().split(" "))
        b = map(int,raw_input().split(" "))

        results.append(solve(a,b,n,k))
    for result in results:
        print result
