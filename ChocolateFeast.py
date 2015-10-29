_author__ = 'deveshbajpai'

'''
Problem Url: https://www.hackerrank.com/challenges/chocolate-feast

Algorithm: For the given n,c and m, firstly calculate the direct available choclates in chocs. Wrappers is equal to
chocolates right now. Now, if the wrappers is more than equal to the discount count (m), get the current extra chocolates
by dividing wrappers available with m. Increment the total extra count with this value (extra_new). Update the wrappers
to be remaining still wrapped chocolates, which includes the modulus of wrappers with m and new extra chocolates (extra_new)
Keep doing this till the count of wrapped chocolates is equal or greater than discount count (m).
In the end, add the grand total of extra to the original chocolates count. Return this value as the final answer.
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
