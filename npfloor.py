import numpy as np 


# A = list(map(float, input().split()))
A = np.array(input().split(),float)
B = np.floor(A)
C = np.ceil(A)
D = np.rint(A)
print(B)
print(C)
print(D)