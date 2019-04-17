# def split(str1, num):
#     return [ str1[start:start+num] for start in range(0, len(str1), num) ]
from collections import deque

class Point:
    def __init__(self, x,y):
        self.x = x
        self.y = y

    def __str__(self):
        return "X=%d,Y=%d"%(self.x,self.y)

def getPointsFromPoint(N,arr,point):
    x = point.x
    y = point.y 
    points=[]

    while x>0:
        x-=1
        if arr[x][y]=='X':
            break
        points.append(Point(x,y))

    x = point.x
    while x<N-1:
        x+=1
        if arr[x][y]=='X':
            break
        points.append(Point(x,y))     

    x = point.x
    while y>0:
        y-=1
        if arr[x][y]=='X':
            break
        points.append(Point(x,y))

    y = point.y
    while y<N-1:
        y+=1
        if arr[x][y]=='X':
            break
        points.append(Point(x,y)) 
    
    return points

def getPath(n,arr,start,end):
    q = deque([start])
    arr[start.x][start.y]=0

    while q:
        current_point = q.pop()
        current_distance = arr[current_point.x][current_point.y]

        points= getPointsFromPoint(n,arr,current_point)
        for p in points:
            if arr[p.x][p.y]=='.':
                arr[p.x][p.y] = current_distance + 1
                q.appendleft(p)
                if p.x == end.x and p.y == end.y :
                    return current_distance + 1
    return -1

    



n = int(input())
row =[0]*n
for i in range(n):
    row[i] = list(input())
    print(row)
startX,startY,goalX,goalY = map(int,input().split())

print(getPath(n,row,Point(startX,startY),Point(goalX,goalY)))
