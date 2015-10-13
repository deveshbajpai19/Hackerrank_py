__author__ = 'deveshbajpai'

'''
Problem Url: https://www.hackerrank.com/challenges/the-love-letter-mystery

Algorithm: Iterate over each string, and keep 2 pointers. First one iterates in forward direction and the later in
backward direction. Find the absolute difference of ASCII values of characters at those pointers to a variable which
stores the total number of changes in the string to make it reduced palindrome. This variable is the final answer.
'''

def solve(input):
    changes = 0
    fwd = 0
    bck = len(input)-1

    while(fwd<bck):
        changes += abs(ord(input[fwd])-ord(input[bck]))
        fwd += 1
        bck -= 1
    return changes




if __name__ == "__main__":
    cases = int(input())
    results = []
    for case in range(cases):
        results.append(solve(raw_input()))
    for result in results:
        print result