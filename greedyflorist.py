[N, K] = map(int, input().split())
C = list(map(int, input().split()))
C = sorted(C, reverse = True)
res = count = x = 0
flag = True
while flag:
    for i in range(K):
        res += (x+1) * C[count]
        count += 1
        if count == N:
            flag = False
            break
    x += 1
print(res)