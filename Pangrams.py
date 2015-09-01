__author__ = 'deveshbajpai'
'''
Problem Url: https://www.hackerrank.com/challenges/pangrams

Algorithm: Obtain a string of all alphabets of english. Iterate over them and check their presence in the given
string. For any absence, return not pangram message. After the loop, return pangram for the true case.
'''
import string
allTheLetters = string.lowercase

def solve(s):
    for alphabet in allTheLetters:
        if alphabet not in s:
            return "not pangram"
    return "pangram"

if __name__ == "__main__":
    s = raw_input()
    print solve(s.lower())