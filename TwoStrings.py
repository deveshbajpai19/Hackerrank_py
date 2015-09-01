__author__ = 'deveshbajpai'
'''
Problem Url: https://www.hackerrank.com/challenges/two-strings

Algorithm: The problem boils down to find if there exists at least one common character between the 2 strings.
Sort the strings alphabetically. Run a loop over both strings and check if their current character is same. If so,
return YES. Else, check which of the 2 characters is smaller alphabetically. Advance the index of that string.
In the default case after the loop return NO as not a single common character exists between the strings.
'''

def solve(a,b):
    a = ''.join(sorted(a))
    b = ''.join(sorted(b))
    #print a
    #print b
    i = j = 0
    while(i<len(a) and j<len(b)):
        if(a[i]==b[j]):
            return "YES"
        elif(a[i]<b[j]):
            i+=1
        else:
            j+=1
    return "NO"

if __name__ == "__main__":
    cases = int(input())
    results = []
    for case in range(cases):
        a = raw_input()
        b = raw_input()
        results.append(solve(a,b))
    for result in results:
        print result
