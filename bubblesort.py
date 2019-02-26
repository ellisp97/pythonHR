#!/bin/python3
import math
import os
import random
import re
import sys

"""attempt 1 not actually bubble sort """
# def countSwaps(a):
#     count = 0
#     for i in range(len(a)):
#         if not (a[i] == i+1):
#             for j in range(i+1,len(a)+1):
#                 if a[j] == i+1:
#                     # print(a)
#                     a[i],a[j] = a[j],a[i]
#                     count+=1
#                     break

#     return a,count
    # pass

# {4,2,3,1}
# for i ,[0,1,2,3]
# for j,[0,1,2]
# a[0] =4 > a[1] =2 , count = 1, {2,4,3,1}
# a[1] = 4>a[2] = 3, count = 2, {2,3,4,1}
# {2,3,1,4}

def countSwaps(a):
    count=0
    for i in range(len(a)):
        for j in range(len(a)-1):
            if (a[j]>a[j+1]):
                count+=1
                a[j],a[j+1]=a[j+1],a[j]

    return a,count



if __name__ == '__main__':
    n = int(input())
    arr = list(map(int,input().split()))
    newArr,count = countSwaps(arr)
    print("Array: {}".format(newArr))
    print("Array is sorted in {} swaps.".format(count))
    print("First Element: {}".format(newArr[0]))
    print("Last Element: {}".format(newArr[len(newArr)-1]))


# {4,5,1,3,2}
# {4,5,1,3,2}