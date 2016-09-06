__author__ = 'Devesh Bajpai'

'''
Problem Url: https://www.hackerrank.com/challenges/mandragora

Algorithm: For every Mandragora, we can either defeat (S++) or battle (P += S*H_i). And we deal with them in any order.
Hence, sort the array of h in ascending more. Now, the base case of max experience points will be when we battle all
the Mandragoras. Hence, total experience points in this case would be S*(H_0 + H_1 + ... H_n). Hence we sum the h array
and take max as this value. Now, we will one by one remove H_i from this sum and consider the case, if we battle all
Mandragoras from 0 to i and battle the rest of them. Why? Since array of h is sorted in ascending order, the larger
H values are towards the end. We will always get a bigger number my multiplication with the larger h_i's in the end.
Hence, we remove the h_i from the sum and see the max of i+2 * sum_h which will be total experience points in this case
and the running value of max. Note, we do i+2 because S starts with value 1 and other 1 is for index of h being 1 less
than actual count.

Example: For given input we have to see the max of these values:
CASE A: 1 * (2 + 2 + 3) = 7
CASE B: 2 * (2 + 3) = 10
CASE C: 3 * (3) = 9

Answer is CASE B.
'''

def solve(n,h):
    h.sort()
    sum_h = sum(h)
    max_h = sum_h
    for i in xrange(0,len(h)):
        sum_h -= h[i]
        max_h = max((i+2) * sum_h, max_h)
    return max_h

if __name__ == "__main__":
    cases = int(input())
    results = []
    for case in range(cases):
        n = int(input())
        h = map(int,raw_input().split(" "))
        results.append(solve(n,h))
    for result in results:
        print result
