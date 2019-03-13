n = int(input())
T = []
for i in range(n):
    order,prep = map(int, input().split())
    T.append([i,prep+order])

T.sort(key=lambda l:l[1])
print(' '.join([str(elem[0]+1) for elem in T]))

