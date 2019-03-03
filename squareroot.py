# Newtons Method
def isqrt(n):
    x = n
    y = (x + 1) // 2
    while y < x:
        x = y
        y = (x + n // x) // 2
    return x
# This returns the largest integer x for which x * x does not exceed n. 

n =int(input())
ans = isqrt(n)
print(ans)