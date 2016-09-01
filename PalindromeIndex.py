__author__ = 'deveshbajpai'

def solve(input):

    change_index = -1
    fwd = 0
    bck = len(input)-1

    if(len(input)==1):
        return change_index

    if(len(input)==2):
        if(input[0]!=input[1]):
            return 0
        else:
            return change_index

    while(fwd<bck):
        if(input[fwd]!=input[bck]):
            if(input[fwd]!=input[fwd+1]):
                change_index = fwd
                break
            elif(input[bck]!=input[bck-1]):
                change_index = bck
                break
        fwd += 1
        bck -= 1
    return change_index




if __name__ == "__main__":
    cases = int(input())
    results = []
    for case in range(cases):
        results.append(solve(raw_input()))

    for result in results:
        print result