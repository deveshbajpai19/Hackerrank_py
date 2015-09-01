__author__ = 'deveshbajpai'
'''
Problem Url: https://www.hackerrank.com/challenges/game-of-thrones

Algorithm: Build the frequency map of characters in the string.
Check the frequency of each character. If it is odd, increment the counter that maintains the quantity of odd frequency
characters. At any instance, it becomes greater than 1, return NO. As a default case, return YES.
'''
from collections import Counter

def solve(s):
    l = s.__len__()
    oddFreqCount = 0
    freqMap = Counter(s)
    for key in freqMap.iterkeys():
        if(freqMap[key]%2==1):
            oddFreqCount+=1
        if(oddFreqCount>1):
            return "NO"
    return "YES"

if __name__ == "__main__":
    s = raw_input()
    print solve(s)