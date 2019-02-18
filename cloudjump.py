def jumpingOnClouds(c):
    # cumulus = curr cloud + 1 or 2
    n = len(c)
    jumpArr = [0]
    i=0
    score=0
    while i+2<n:
        if c[i+2] ==1:
            if c[i+1] ==0:
                jumpArr.append(i+1)
                i+=1
                continue
        else:
            jumpArr.append(i+2)
            i+=2

    if i<n-1:
        score = len(jumpArr)
    else:
        score = len(jumpArr)-1

    # print(jumpArr) 
    print(score) 
        
    return

if __name__ == '__main__':
    n = input()
    c = list(map(int, input().split()))
    result = jumpingOnClouds(c)
