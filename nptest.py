import numpy as np



N ,M = input().split()
# print(N)
A=list(map(int,input().split()))
# A=np.array(A,int)
B=list(map(int,input().split()))
# B=np.array(B,int)

print(np.add(A,B))
print(np.subtract(A,B))
print(np.multiply(A,B))
print(np.divide(A,B))
print(np.mod(A,B))
print(np.power(A,B))