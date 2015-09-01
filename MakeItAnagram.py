__author__ = 'deveshbajpai'
'''
Problem Url: https://www.hackerrank.com/challenges/make-it-anagram/

Algorithm: Build the frequency map of 2 strings. Getting the difference of them will get characters which are uncommon
between them. freqMap1-freqMap2 gives the characters which are present in freqMap1 but not in freqMap2. Similarly,
freqMap2-freqMap1 gives the characters which are present in freqMap2 but not in freqMap1. Run over these difference maps
and calculate the total difference.
'''
from collections import Counter

def solve(str1,str2):
    diff = 0
    str1 = ''.join(sorted(str1))
    str2 = ''.join(sorted(str2))
    freqMap1 = Counter(str1)
    freqMap2 = Counter(str2)
    freqMap3 = freqMap1-freqMap2
    freqMap4 = freqMap2-freqMap1
    for key in freqMap3:
        diff+=freqMap3[key]
    for key in freqMap4:
        diff+=freqMap4[key]
    return diff

if __name__ == "__main__":
    str1 = raw_input()
    str2 = raw_input()
    print solve(str1,str2)
