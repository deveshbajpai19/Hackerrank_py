__author__ = 'deveshbajpai'
'''
Problem Url: https://www.hackerrank.com/challenges/utopian-tree

Algorithm: The solution is straightforward. For each tree, run a loop for the number of cycles. For every odd cycle,
increment the tree height by 1, and for even cycle, double it. Return the final tree height.
'''


def solve(cycles):
    tree = 1
    for cycle in xrange(1,cycles+1):
        if(cycle%2==0):
            tree += 1
        else:
            tree *= 2

    return tree

if __name__ == "__main__":
    cases = int(input())
    results = []
    for case in range(cases):
        results.append(solve(int(raw_input())))
    for result in results:
        print result
