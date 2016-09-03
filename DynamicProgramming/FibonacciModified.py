__author__ = 'deveshbajpai'
'''
https://www.hackerrank.com/challenges/fibonacci-modified

Algorithm: Straightforward. Almost same as regular fibonacci problem, except the square term of one previous element.
I used long to take care of overflow over the range of a 64-bit integer.
'''


def solve(t1,t2,n):

    #base case
    if n == 0:
        return t1
    elif n == 1:
        return t2

    #initialize dp array
    dp = [t1,t2] + [0] * (n-2)

    #bottom up computation of dp array
    for i in xrange(2,n):
        dp[i] = long(dp[i-2]) + pow(long(dp[i-1]),2)

    return dp[n-1]


if __name__ == "__main__":
    t1,t2,n = map(long,raw_input().split(" "))
    print solve(t1,t2,n)