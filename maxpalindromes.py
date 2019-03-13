from collections import Counter
def maxPalindrome(s,l,r):
    noMaxPalindromes = 0
    cnt = Counter(s)
    # case where no letter appears more than once
    if max(cnt.values()) < 2:
        return len(cnt)

    print(max(cnt.values()))
    print(noMaxPalindromes)
    newStr = s[l:r]

    return noMaxPalindromes



if __name__ == '__main__':
    s = input()
    q = int(input())
    for i in range(q):
        l,r = map(int, input().split())
        result = maxPalindrome(s, l-1, r+1)
        print(result)

#  Sample Input 0

# week
# 2
# 1 4
# 2 3
# Sample Output 0

# 2
# 1
# Explanation 0

# On the first day, l=1 and r=4. The maximum-length palindromes are "ewe" and "eke".

# On the second day, l=2 and r=3. The maximum-length palindrome is "ee".