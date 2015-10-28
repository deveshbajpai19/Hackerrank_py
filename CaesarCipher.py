_author__ = 'deveshbajpai'

'''
Problem Url: https://www.hackerrank.com/challenges/caesar-cipher-1

Algorithm: Interesting problem. For the given word, iterate over it's length. For each character, check whether it
falls in the ASCII ranges of either lowercase or upper case alphabets. This can also be done using isAlpha() function.
Keep 2 variables, base and end to note the ASCII range-end values for the current character. If it is alphabet and not
a special character, increase the ASCII value of it by the given rotation value (k). If it crosses the end-range value
of ASCII (end), find the offset of the overflow from the base. Obtain the character for that ASCII value and append to
 the output string. After the word iteration, return the new output string.

 Note, it is important to check if k is more than the total number of characters (26) at the start of any processing.
 See the comment below in the code for justifications.
'''

def solve(word,n,k):
    base = 0
    end = 0
    new_word = ""
    #If k is more than 26, the rotation will have to wrapped again through the same alphabet sequence.
    #Hence this helps to take care of superfluous rotations, and bright it back to effective 26 letter rotation
    k %= 26
    for i in xrange(0,n):
        char = word[i]

        if(char>='a' and char<='z'):
            base = 97
            end = 122
        elif(char>='A' and char<='Z'):
            base = 65
            end = 90
        if(base==97 or base==65):
            new_ord = ord(char)+k
            if(new_ord>end):
                new_ord = base+(new_ord-end)-1
            char = chr(new_ord)
        new_word += char
        base = 0
        end = 0
    return new_word




if __name__ == "__main__":
    n = int(input())
    word = raw_input()
    k = int(input())
    print solve(word,n,k)
