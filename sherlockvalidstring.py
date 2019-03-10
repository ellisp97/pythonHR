# str1 = input().strip()
# lettercounts = {}
# for letter in str1:
#     if letter not in lettercounts:
#         lettercounts[letter] = 1
#     else:
#         lettercounts[letter] += 1
# flag=True
# incorrect = 0
# # print(list(lettercounts.values()))
# const = list(lettercounts.values())[0]
# for value in list(lettercounts.values()):
#     if not const == value:
#         if (value == const+1) or (value == const-1):
#             incorrect += 1
#         flag = False
    
# if flag | incorrect==1:
#     print("YES")
# else:
#     print("NO")

# or use a hash-map in solution below
from collections import Counter

def isValid(s):
    cnt = Counter(s)
    print(cnt)
    print(cnt.values())
    print(set(cnt.values()))
    if len(set(cnt.values())) == 1:
        return "YES"
    elif len(set(cnt.values())) > 2:
        return "NO"
    else:
        m1 = max(cnt.values())
        m2 = min(cnt.values())
        if list(cnt.values()).count(m2) == 1:
            return "YES"
        if list(cnt.values()).count(m1) > 1 or m1 - m2 > 1:
            return "NO"
        return "YES"

s = input().strip()
result = isValid(s)
print(result)