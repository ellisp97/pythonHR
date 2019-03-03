def Merge(L,R,A):
    i,j,k = 0,0,0
    while i < len(L) and j < len(R):
            if L[i] < R[j]:
                A[k]=L[i]
                i=i+1
            else:
                A[k]=R[j]
                j=j+1
            k=k+1
    while i < len(L):
        A[k]=L[i]
        i=i+1
        k=k+1
    while j < len(R):
        A[k]=R[j]
        j=j+1
        k=k+1

def MergeSort(A):
    n = len(A)
    if n<2:
        return 
    mid = n//2
    lefthalf = A[:mid]
    righthalf = A[mid:]

    MergeSort(lefthalf)
    MergeSort(righthalf)
    Merge(lefthalf,righthalf,A)

A = list(map(int, input().split()))
MergeSort(A)
print(A)