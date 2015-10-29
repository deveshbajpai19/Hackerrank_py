_author__ = 'deveshbajpai'

'''
Problem Url: https://www.hackerrank.com/challenges/cavity-map

Algorithm: Biggest take-away from this problem's solution is that strings by default are immutable in Python.
So, if you want to make editions to it, use bytearray. For the grid, which a DD array, run 2 loops by making sure
you avoid the boundary elements. Now, for every cell, compare it's value against it's neighbors. If greater than all,
assign X at that cell. Return the reformed grid in the end.
PS: Taking the int of the cell value which is coming from array of bytearrays would give it's ASCII value. But since,
everything is relative, the calculations work fine. And X has a way-larger ASCII value (88). Hence, no need to worry!
'''

def solve(grid,n):


    for i in xrange(1,n-1):
        for j in xrange(1,n-1):
            cur = int(grid[i][j])
            left = int(grid[i][j-1])
            right = int(grid[i][j+1])
            top = int(grid[i-1][j])
            bottom = int(grid[i+1][j])

            if(cur>left and cur>right and cur> top and cur>bottom):
                grid[i][j] = 'X'

    return grid




if __name__ == "__main__":
    n = int(input())
    grid = []
    for _n in xrange(n):
        grid.append(bytearray(raw_input()))
    grid = solve(grid,n)

    for line in grid:
        print line