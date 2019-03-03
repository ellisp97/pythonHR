def BinarySearch(A,n,x):
    low =0
    high = n-1
    while  (low<=high):
        mid = (low+high)//2
        if x == A[mid]:
            return mid
        elif x <A[mid]:
            high = mid - 1
        else:
            low = mid+1
    return -1


x = int(input())
A = list(map(int,input().split()))
n = len(A)
mid = BinarySearch(A,n,x)
print("The mid position is: ",mid)