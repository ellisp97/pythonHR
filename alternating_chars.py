n = int(input())
for _ in range(n):
    s = input()
    delete_cnt = 0
    for i in range(1,len(s)):
        if s[i] == s[i-1]:
            delete_cnt +=1
    print(delete_cnt)

# Sample Input

# 5
# AAAA
# BBBBB
# ABABABAB
# BABABA
# AAABBB
# Sample Output

# 3
# 4
# 0
# 0
# 4
# Explanation

# number of deletions required to make string so there are no adjacent chars matching