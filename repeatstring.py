import sys


s = nput().strip()
n = long(input().strip())
n_of_a = 0
for i in s:
    if i == 'a':
        n_of_a += 1
res = n_of_a * (n / len(s))
for i in s[:n % len(s)]:
    if i == 'a':
        res += 1
print(res)
# wwayy better 
    s, n = input().strip(), int(input().strip())
    print(s[:2])
    print(s.count("a") * (n // len(s)) + s[:n % len(s)].count("a"))

# Sample Input 0

# aba
# 10
# Sample Output 0

# 7