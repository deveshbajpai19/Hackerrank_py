__author__ = 'Devesh Bajpai'

import sys
'''
Problem Url: https://www.hackerrank.com/challenges/array-splitting

Algorithm: Idea is to binary search. For every sub array that is considered, we use left and right sum. Left sum
is the sum of elements from start to current element, and right sum is the sum of elements from next of current element
to the last one. If at any index we find the equilibrium for sums, we divide it further and check for its sub arrays.
The max of them is considered. This recurrence will give the final total points that can be earned.
'''

def solve(a,left,right,rightSum):

    if left == right:
        return 0

    leftSum = 0
    for i in xrange(left,right):
        leftSum += a[i]
        rightSum -= a[i]

        if leftSum == rightSum:
            return 1 + max(solve(a,left,i,leftSum), solve(a,i+1,right,rightSum))

    return 0

if __name__ == "__main__":

    #this helps for the time-out issues in certain testcases
    sys.setrecursionlimit(20000)
    cases = int(input())
    results = []

    for case in range(cases):
        n = int(input())
        a = map(int,raw_input().split(" "))
        results.append(solve(a,0,n-1,sum(a)))
    for result in results:
        print result
