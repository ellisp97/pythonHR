import numpy as np 

# A = list(map(float, input().split()))
N,M = map(int, input().split())

A = np.array(input().split(), int)
B = np.array(input().split(), int)
newarr = np.array([A,B])
C = np.sum(newarr,axis=0)
# print(C)
print(np.prod(C))


# A = numpy.array([list(map(int, input().split())) for n in range(N)])
