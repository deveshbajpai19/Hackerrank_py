__author__ = 'deveshbajpai'

'''
https://www.hackerrank.com/challenges/red-john-is-back

Algorithm: Bricks available are either 4x1 or 1x4. Wall is 4xN
The question wants to know number of primes till the number k where k denotes the number of ways to put bricks
in a wall of 4xN. Finding the number of primes till k is straightforward using sieve of eratosthenes.

Let's see how to solve the for k.
There are 2 cases in which we can fill the wall using either bricks. Let F(n) give the no. of ways to put bricks in
a wal of 4xN
CASE 1: Using 1 4x1 brick
We would then have F(n-1) ways

CASE 2: Using 4 1x4 bricks
We would then have F(n-4) ways

So total number of ways is F(n-1) + F(n-4)

Once the F(n) is calculated using bottom-up technique, we pass F(n) to sieve of eratosthenes method to calculate the
number of primes till it. That is the final answer.
'''

def solve(n):

    #base case: number of ways to put bricks in a wall of 4x1/4x2/4x3 is 1 (since bricks are 4x1 or 1x4)
    #so the number of primes till 1 is 0 (since 1 itself isn't prime
    if n <= 3:
        return 0

    dp = [0] * (n+1)

    dp[0] = dp[1] = dp[2] = dp[3] = 1

    #bottom-up DP computation
    for i in xrange(4,n+1):
        dp[i] = dp[i-1] + dp[i-4]

    return len(list(solve_prime_sieve(dp[n])))

#utility method to calculate primes till n
def solve_prime_sieve(n):
    multiples = set()
    for i in xrange(2, n+1):
        if i not in multiples:
            multiples.update(xrange(i*2, n+1, i))
            yield i


if __name__ == "__main__":
    cases = int(input())
    inputs = []
    results = []
    for case in range(cases):
        n = int(input())
        results.append(solve(n))
    for result in results:
        print result
