import math

n, goal = map(int, input().split())
machines = list(map(int,input().split()))


def minTime(machines, goal):
    minday = math.ceil(goal / len(machines)) * min(machines)
    maxday = math.ceil(goal / len(machines) * max(machines))
    while minday < maxday:
        day = (maxday + minday) // 2
        if sum(day // m for m in machines) >= goal:
            maxday = day
        else:
            minday = day + 1
    return minday

print(minTime(machines,goal))