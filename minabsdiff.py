import itertools
import math


def compAbs(arr,sizeArr):
        minAbsolute = math.inf
        li= [i for i in itertools.combinations(arr,2)]
        for ele in li:
                if abs(ele[0]-ele[1]) < minAbsolute:
                        minAbsolute = abs(ele[0]-ele[1])
        return minAbsolute

# MANUAL IMPLEMENTATION OF COMBINATIONS
# def combo2(lst,n):
#     if n==0:
#         return [[]]
#     l=[]
#     for i in range(0,len(lst)):
#         m=lst[i]
#         remLst=lst[i+1:]
#         for p in combo2(remLst,n-1):
#             l.append([m]+p)
#     return l
            

if __name__ == '__main__':
    sizeArr = int(input())
    arr = list(map(int,input().split()))
    print(compAbs(arr,sizeArr))
