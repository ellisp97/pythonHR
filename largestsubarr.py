# You are given an array of variable length, which contains
# only following integers: -1, 0, 1. 
# Example A[] = {0, 1, 0, 1, 1, -1, 1} 
# You are also given an integer S. 

# Write a program with O(n) time that can find out the length 
# of the largest sub-array which sums up to S. 
# Example, if S = 2, then the length of the largest sub-array 
# in the above array is 6. 

# If there is no such sub-array that can sum up to S, then output 0.
import math

A = [0, 1, 0, 1, 1, -1, 1]
n = 7
S = 2
sumN = 0
ans = 0
minIndex = [10000]*7
maxIndex = [-10000]*7
minIndex[0] = 0

for i in range(n):
    sumN += A[i]
    minIndex[sumN] = min(minIndex[sumN], i+1)
    maxIndex[sumN] = max(maxIndex[sumN], i+1)

for i in range(n-S):
    # maxIndex[i + S] - minIndex[i] is the maximum length of value i
    ans = max(ans, maxIndex[i+S]- minIndex[i])
print(ans)    