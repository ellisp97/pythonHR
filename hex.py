def print_formatted(N):
    width = len(bin(N)) - 2
    for i in range(1,N+1):
        print("{0:{width}d} {0:{width}o} {0:{width}X} {0:{width}b}".format(i,width = width))
    return
if __name__ == '__main__':
    n = int(input())
    print_formatted(n)



    # 1     1     1     1
    # 2     2     2    10
    # 3     3     3    11
    # 4     4     4   100
    # 5     5     5   101
    # 6     6     6   110
    # 7     7     7   111
    # 8    10     8  1000