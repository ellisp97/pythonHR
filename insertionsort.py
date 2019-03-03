test = list(map(int,input().split()))
n = len(test)
for i in range(1,n):
    value = test[i]
    hole = i
    while(hole>0 and test[hole-1]>value):
        test[hole] = test[hole - 1]
        hole -= 1
    test[hole] = value

print(test)