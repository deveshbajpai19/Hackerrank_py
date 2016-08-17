_author__ = 'deveshbajpai'

'''
Problem Url: https://www.hackerrank.com/challenges/sherlock-and-the-beast

Algorithm: Quite an interesting problem. The solution looks complicated, so let's break it down in simpler chunks.
As seen, this solution is categorized in different type of inputs in the if-else ladder. They are as follow:

1) If n is 1,2 or 4, it is not possible to divide it into divisible components of 3 and 5. Also, since 3 and 5 are
prime numbers, the numbers lesser to them would not be breakable for this solution. Hence, answer is -1.
2) If n is 3 or 5, there is just one possibility to have all digits as 5 or 3 respectively. Again, this is due to 3
and 5 being prime numbers.

Now, we come to cases where n is more than 5. There are 4 possibilities that we could work out:

A) We try to make a number of purely 5s. Since our motto is get the largest number, that seems to be our favorite choice.
If n is a multiple of 3, we have a number of all 5s. And that is your answer.

B) Now come to else component. Our motive here is to get a number starting with 5s and followed with 3s. m3 captures is
the multiple of 3 possible in the number. The loop works till a valid 3's multiple is possible. If the remaining number
which is r, is divisible with 5, we have found the number. The condition r!=n makes sure we do not check the remaining
number to be multiple of 5 for the first time. Why? Well, that may happen if the number is common multiple of 3 and 5.
Being a multiple of 5 will cause it to have more 3s in it, where we could have 5s instead.

C) We keep decreasing m3 in every iteration till it reaches 0. If we bumped into the case where we could not find a number
of the type 5....3...., we can now try for the next possibility: only 3s. This can be checked if failed in the above
iteration (if m3 became 0) and the number n is divisible by 5.

D) The last case; when nothing worked out, we default to the answer being -1.

'''



def solve(n):

    ans = -1

    if(n==1 or n==2 or n==4):
        return ans
    elif(n==3):
        ans = 555
    elif(n==5):
        ans = 33333
    elif(n%3==0):
        ans = '5'*n
    else:
        r = n
        m3 = n/3
        while(m3>0):
            if(r%5==0 and r!=n):
                ans = '5'*(3*m3) + '3'*((r/5)*5)
                break
            else:
                m3-=1
                r = n-(m3*3)

        if(m3==0 and n%5==0):
            ans = '3'*n

    return ans



if __name__ == "__main__":
    cases = int(input())
    results = []
    for case in range(cases):
        results.append(solve(int(input())))
    for result in results:
        print result
