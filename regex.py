# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

n = int(input())                    
for _ in range(n):
    k = input()
    print(bool(re.match(r'^[+-]?\d*?\.{1}\d+$',k)))


# Sample Input
# 4  
# 4.0O0
# -1.00
# +4.54
# SomeRandomStuff
# Sample Output
# False
# True
# True
# False