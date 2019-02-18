n,m = map(int, input().split())
A = [0]*n
arr = [0]*m
maxEle = 0


for i in range(m):
    arr[i]=list(map(int, input().split()))

i=0
while i<m:
    # print("arr[i][0]: {}, arr[i][1]: {}".format(arr[i][0],arr[i][1]))
    for j in range((arr[i][0])-1,arr[i][1]):
        # print("i: {}, j: {}".format(i,j))
        A[j] += arr[i][2]
        if A[j] > maxEle:
            maxEle = A[j]
    i += 1


print(maxEle)


# THEIR SOLN 
n, inputs = [int(n) for n in input().split()]
listN = [0]*(n+1)
for _ in range(inputs):
    x, y, incr = [int(n) for n in input().split()]
    listN[x-1] += incr
    if((y)<=len(listN)):
         listN[y] -= incr
max = x = 0
for i in listN:
    x=x+i
    if(max<x):
        max=x
print(max)

# ===== Format =======
# Sample Input

# 5 3
# 1 2 100
# 2 5 100
# 3 4 100
# Sample Output

# 200



# ===== Example =====
#     a b k
#     1 5 3
#     4 8 7
#     6 9 1
# Add the values of  between the indices  and  inclusive:

# index->	 1 2 3  4  5 6 7 8 9 10
# 	[0,0,0, 0, 0,0,0,0,0, 0]
# 	[3,3,3, 3, 3,0,0,0,0, 0]
# 	[3,3,3,10,10,7,7,7,0, 0]
# 	[3,3,3,10,10,8,8,8,1, 0]

# max value is thus 10