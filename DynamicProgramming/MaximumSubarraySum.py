__author__ = 'deveshbajpai'
'''
Problem Url: https://www.hackerrank.com/challenges/maxsubarray

Algorithm: Algorithm has two parts:
A) Non Contiguous (may or may not be contiguous) - solve_ncont()
Here we may fall into 2 types of scenarios. First, all elements of the array are negative. If so, we need to return
the element closest to 0, or minimum negative (least absolute value but with negative sign)
Second scenario would be when at least one of the element is positive. If so, we need to sum only the positives.
The counter to track the number of negative elements helps to differentiate between the two scenarios

B) Contiguous (strictly contiguous) - solve_cont()
Here we employ the usual DP solution. We maintain an array for holding sub-solutions. dp_sum[i] is the maximum sum of
elements from 0 to i. It is the maximum sum possible via any contiguous sub-array in sub-array 0 to i.
We also keep a track of the maximum sub-array sum calculated so far. That is the final answer.
'''
import sys

#master solve method
def solve(arr, n):

    result_contiguous = solve_cont(arr, n)
    result_noncontiguous = solve_ncont(arr, n)

    return str(result_contiguous)+" "+str(result_noncontiguous)

#part A: Non Contiguous
def solve_ncont(arr, n):
    negativePresent = 0
    maxSumOnlyPositive = 0
    #lower limit for integer values
    minNegative = -sys.maxint - 1

    for a in arr:
        if a < 0:
            negativePresent += 1
            minNegative = max(minNegative, a)
        else:
            maxSumOnlyPositive += a

    if negativePresent == n:
        return minNegative
    else:
        return maxSumOnlyPositive

#part B: Contiguous
def solve_cont(arr, n):

    dp_sum = [0] * n
    dp_sum[0] = arr[0]
    max_sum = arr[0]
    for x in xrange(1,n):
        dp_sum[x] = max(arr[x], dp_sum[x-1] + arr[x])
        max_sum = max(max_sum, dp_sum[x])

    #print dp_sum
    return max_sum

if __name__ == "__main__":
    cases = int(input())
    inputs = []
    results = []
    for case in range(cases):
        n = int(input())
        result = solve(map(int,raw_input().split(" ")), n)
        results.append(result)
    for result in results:
        print result