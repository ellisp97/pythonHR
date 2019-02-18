def rotLeft(arr, d):
    for i in range(d):
        newEle = arr.pop(0)
        arr += [newEle]
    print(' '.join(map(str, arr)))
    return

if __name__ == '__main__':
    n,d = map(int, input().split())
    arr = list(map(int,input().split()))
    rotLeft(arr, d)
