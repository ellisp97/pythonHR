from collections import Counter

def count_anagrams(string):
    buckets = {}
    for i in range(len(string)):
        for j in range(1, len(string) - i + 1):
            # unordered immutable version of a set, used as keys for dictionaries
            key = frozenset(Counter(string[i:i+j]).items()) # O(N) time key extract
            # get if cant find in bucket defaults to 0
            buckets[key] = buckets.get(key, 0) + 1
    count = 0
    for key in buckets:
        # Triangular Numbers to count anagram pairs using this formula below
        count += buckets[key] * (buckets[key]-1) // 2
    return count

n = int(input())
for i in range(n):
    s = input().strip()
    print(count_anagrams(s))

# Sample Input 0

# 2
# abba
# abcd
# Sample Output 0

# 4
# 0
# Explanation 0

# The list of all anagrammatic pairs is  and  at positions  and  respectively.

# No anagrammatic pairs exist in the second query as no character repeats.