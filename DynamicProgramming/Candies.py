__author__ = 'deveshbajpai'
'''
https://www.hackerrank.com/challenges/candies

Algorithm: 2 important points in this question. A student has to be compared with his/her neighbor on the left
and right. So we maintain 2 DP arrays to track it. While computing dp_left, we move left to right over the ratings
and see, if the current student's rating is more than that of his left neighbor, we increase the candy count by 1 for
this student. Similarily we compute the dp_right array by moving right to left. Finally for ith index in dp_left and
dp_right, we will have the candies needed for ith student wrt when compared to his left and right neighbors respectively.
To consider his/her final candy count, we will take max of both values. Keep a variable to sum all these values and
return it as a final answer. Note, as a default we give 1 candy to each student. Hence, DP arrays are initialized as 1.
'''
def solve(ratings):

    if len(ratings) == 0:
        return 0
    all = 0
    dp_left = [1] * n
    dp_right = [1] * n

    #calculate dp_left (wrt student on the left)
    for i in xrange(1,len(ratings)):
        if ratings[i-1] < ratings[i]:
            dp_left[i] = dp_left[i-1]+1

    #calculate dp_right (wrt student on the right)
    for i in xrange(len(ratings)-2,-1,-1):
        if ratings[i+1] < ratings[i]:
            dp_right[i] = dp_right[i+1]+1

    #calculate the max of dp_left and dp_right for all
    for i in xrange(0,len(ratings)):
        all += max(dp_left[i],dp_right[i])

    return all


if __name__ == "__main__":
    n = int(input())
    ratings = []
    for _n in range(n):
        ratings.append(int(input()))
    print solve(ratings)

