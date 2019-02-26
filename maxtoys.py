
N,K = map(int, input().strip().split())
assert 1 <= N <= 10**5 and 1 <= K <= 10**9

lis = map(int, input().strip().split())
for toy in lis:
    assert 1 <= toy <= 10**5
    
lis.sort()
    
count = 0
for i in range(N-1):
    K -= lis[i]
    if K < 0:
        print(count)
        exit(0)
    else:
        count += 1
    
print(count)






# he wants to maximize the number of toys he buys with this money.
# Given a list of prices and an amount to spend, what is the maximum number of toys Mark can buy? For example, 


# prices: an array of integers representing toy prices
# k: an integer, Mark's budget

# The first line contains two integers,  and , the number of priced toys and the amount Mark has to spend. 
# The next line contains  space-separated integers 

# A toy can't be bought multiple times.

# Output Format

# An integer that denotes the maximum number of toys Mark can buy for his son.

# Sample Input

# 7 50
# 1 12 5 111 200 1000 10
# Sample Output

# 4
