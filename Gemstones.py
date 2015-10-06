__author__ = 'deveshbajpai'

'''
Problem Url: https://www.hackerrank.com/challenges/gem-stones

Algorithm: Iterate over each string, find the unique characters in it by storing its characters in a set and
create a frequency map of characters in it using Counter collection. Add this frequency map to the master map
called char_map. Now, iterate over this master map and check for every key (character) if its value is equal
to the number of string. If so, it is a gem-element; increase the result. At the end, return result.
'''

from collections import Counter

def solve(inputs,cases):
    char_map = Counter()
    result = 0
    for input in inputs:
        char_map += Counter(set(''.join(input)))

    for key in char_map.iterkeys():
        if(char_map[key]==cases):
            result +=1

    return result




if __name__ == "__main__":
    cases = int(input())
    inputs = []
    for case in range(cases):
        inputs.append(raw_input())
    print solve(inputs,cases)