# f = open('test.txt', 'r')
# print(f.read())
import math

noContests, maxLose = map(int, input(). split())
dictArr = {}
disc = []
for i in range(noContests):
    luckArr, importArr = map(int, input().split())
    dictArr[i] = ([luckArr,importArr])

# print(dictArr)
minIndex = [i[0] for _,i in dictArr.items() if i[1]==1]
maxIndex = [i[0] for _,i in dictArr.items() if i[1]==0]

minIndex.sort()
# print(minIndex)
for i in range(len(minIndex)-maxLose):
    if len(minIndex)>0:
        disc.append(minIndex.pop(0))
# print(minIndex)
print(sum(minIndex)+sum(maxIndex)-sum(disc))

# f.close()