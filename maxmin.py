import math
N = int(input())
K = int(input())
lis = []
for i in range(N):
    lis.append(int(input()))
    
lis.sort()   
answer = math.inf
    
for index in range(N-K+1):
    diff = lis[index+K-1] - lis[index]
    if diff < answer:
        answer = diff
    
print(answer)