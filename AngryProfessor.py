__author__ = 'deveshbajpai'

def solve(n,k,students):

    _k = 0
    for student in students:

        if(student<=0):
            k-=1
            if(k==0):
                return "NO"
    if(k>0):
        return "YES"




if __name__ == "__main__":
    cases = int(input())
    results = []
    for case in range(cases):
        n,k = map(int,raw_input().split(" "))
        students = map(int,raw_input().split(" "))
        results.append(solve(n,k,students))

    for result in results:
        print result