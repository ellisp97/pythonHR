# 4 4 4 4 4 4 4 
# 4 3 3 3 3 3 4 
# 4 3 2 2 2 3 4 
# 4 3 2 1 2 3 4 
# 4 3 2 2 2 3 4 
# 4 3 3 3 3 3 4 
# 4 4 4 4 4 4 4 
def print_line(n,num):
    low = abs(n)
    print(' '.join(str(max(low + 1, abs(i) + 1)) for i in range(-num + 1, num)))


def pretty_print(num):
    for i in range(-num + 1, num):
        print_line(i,num)

n = int(input())
pretty_print(n)