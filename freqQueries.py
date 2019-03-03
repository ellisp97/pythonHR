# #   ------- First Attempt --------
# n = int(input())
# A=[]
# for i in range(n):
#     command,val = map(int,input().split())
#     if command == 1:
#         A.append(val)
#     elif command == 2:
#         if val in A:
#             A.remove(val)
#     elif command ==3:
#         flag = False
#         for j in range(n):
#             if A.count(j) == val:
#                 print(1)
#                 flag = True
#                 break
#         if not flag:
#             print(0)
        
# #  ------- Optimal Solutions -------
from collections import defaultdict
n = int(input())

data_freq_dict = defaultdict(int)

for tc in range(n):
    op, data = map(int, input().strip().split())

    if op == 1:
        # insert
        data_freq_dict[data]+=1

    elif op == 2:
        # delete
        if data in data_freq_dict:
            data_freq_dict[data] -= 1

        data_freq_dict[data]  = 0 if data_freq_dict[data] < 0 else data_freq_dict[data]

    else:
        # check if any key in data_freq_dict has count = data         
        print('1' if data in set(data_freq_dict.values()) else '0')

# =======================================
# Sample Input 0

# 8
# 1 5
# 1 6
# 3 2
# 1 10
# 1 10
# 1 6
# 2 5
# 3 2
# Sample Output 0

# 0
# 1
# Explanation 0

# For the first query of type 3, there is no integer whose frequency is 2 (array=[5,6]).
# So answer is 0. For the second query of type 3, there are two integers in array=[6,10,10,6,5]
# whose frequency is 2 (integers = 6 and 10). So, the answer is 1.