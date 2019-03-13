import os
import sys

def highestValuePalindrome(str1, n, k):
    pos = []
    p = []
    for i in range(0, n // 2):
        # accesses list [x,,,,,,x] going inwards per iteration
        if str1[i] != str1[-1 - i]:
            # if no changes are allowed and list elements differ in palindrome fromar
            if k == 0: return "-1"
            # decrease number of changes allowed
            k -= 1
            # find maximum digit in above format
            p += max(s[i], s[-1 - i])
            # record the position of change [x,,,,,,,]
            pos.append(i)
        else:
            # if string match copy the original string as normal
            p += s[i]

    # print(p)
    # print(pos)



    i = 0
    # while there are changes to be made and i hasnt exceeded list length
    # in the event not all k moves are used
    while k > 0 and i < len(p):
        if p[i] != '9':
            if i in pos:
                p[i] = '9'
                k -= 1
            elif k >= 2:
                p[i] = '9'
                k -= 2
        i += 1

    if n % 2 == 1:
        if k >= 1:
            p += '9'
        else:
            p += s[n // 2]

    if n % 2 == 1:
        p = p + p[-2::-1]
    else:
        p = p + p[::-1]

    return ''.join(p)


if __name__ == '__main__':
    n, k = map(int, input().split())
    s = input()
    result = highestValuePalindrome(s, n, k)
    print(result)


    
# Sample Input 0

# 4 1
# 3943
# Sample Output 0

# 3993