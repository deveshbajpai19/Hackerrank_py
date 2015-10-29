_author__ = 'deveshbajpai'

'''
Problem Url: https://www.hackerrank.com/challenges/find-digits

Algorithm: For each number, iterate over it's digits. This is done by doing a modulus with 10 to obtain the digit
and then dividing it by 10 to move to next digit. It works from right to left. Check for each digit that it is firstly
not zero, and divides completely the original number. Return the total count and the end of the loop.
'''

def solve(n,c,m):
    chocs = 0
    extra = 0
    extra_new = 0
    chocs = n/c
    wrappers = chocs

    while(wrappers>=m):
        extra_new = wrappers/m
        extra += extra_new
        wrappers = wrappers%m + extra_new
    chocs += extra

    return chocs




if __name__ == "__main__":
    cases = int(input())
    results = []
    for case in range(cases):
        n,c,m = map(int,raw_input().split(" "))
        results.append(solve(n,c,m))
    for result in results:
        print result
