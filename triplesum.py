A, B, C = map(int, input().split())
arrA = list(map(int,input().split()))
arrB = list(map(int,input().split()))
arrC = list(map(int,input().split()))

def triplets(a,b,c):
    a = list(sorted(set(a)))
    b = list(sorted(set(b)))
    c = list(sorted(set(c)))
    
    ai,bi,ci,ans = 0,0,0,0

    while bi < len(b):
        while ai < len(a) and a[ai] <= b[bi]:
            ai += 1
        
        while ci < len(c) and c[ci] <= b[bi]:
            ci += 1
        
        ans += ai * ci
        bi += 1
    return ans

print(triplets(arrA,arrB,arrC))



