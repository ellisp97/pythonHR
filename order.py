from operator import itemgetter

N = int(input())
Human = [0]*N
for i in range(N):
    Human[i] = list(map(str,input().split()))
    print(Human[i])

sortHumans = sorted(Human,key=itemgetter(2))
print(sortHumans)
for i in range(N):
    if sortHumans[i][3] == 'M':
        print("Mr. {} {}".format(sortHumans[i][0], sortHumans[i][1]))
    else: 
        print("Ms. {} {}".format(sortHumans[i][0], sortHumans[i][1]))




# Sample Input

# 3
# Mike Thomson 20 M
# Robert Bustle 32 M
# Andria Bustle 30 F
# Sample Output

# Mr. Mike Thomson
# Ms. And3ria Bustle
# Mr. Robert Bustle