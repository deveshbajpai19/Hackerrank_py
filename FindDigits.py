_author__ = 'deveshbajpai'

'''
Problem Url: https://www.hackerrank.com/challenges/find-digits

Algorithm: For each number, iterate over it's digits. This is done by doing a modulus with 10 to obtain the digit
and then dividing it by 10 to move to next digit. It works from right to left. Check for each digit that it is firstly
not zero, and divides completely the original number. Return the total count and the end of the loop.
'''

def solve(num):
    count = 0
    _num = num
    while(_num>0):
        digit = _num%10
        if(digit!=0 and num%digit==0):
            count+=1
        _num /= 10
    return count




if __name__ == "__main__":
    cases = int(input())
    results = []
    for case in range(cases):
        results.append(solve(int(raw_input())))
    for result in results:
        print result
