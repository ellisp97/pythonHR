from collections import defaultdict

n, r = map(int, input().split())
arr = list(map(int, input().split()))

v2 = defaultdict(int)
v3 = defaultdict(int)
count = 0
for k in arr:
    count += v3[k]
    v3[k*r] += v2[k]
    v2[k*r] += 1

print(count)




# Brute force is no good because time complexity O(n^3)
# use common ratio and dictionaries 

# Sample Input 0

# 4 2
# 1 2 2 4
# Sample Output 0

# 2
# Explanation 0

# There are  triplets in satisfying our criteria, whose indices are (0,1,3) and (0,2,3) 