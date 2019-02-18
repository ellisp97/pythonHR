n=int(input())
arr = list(map(int, input().split()))
og = list(range(1,n+1))
swaps = 0
# print(arr)


# for i in range(n):
#     j=i
#     print("This is i:{} and this is j:{}".format(i,j))
#     while arr[j] != og[i]:
#         j+=1
#     arr[j],arr[i] = arr[i], arr[j]
#     swaps +=1


for i in range(n):
    while arr[i] != i + 1:
        print("This is arr[i]:{} and this is i:{}".format(arr[i],i))
        arr[arr[i] - 1], arr[i] = arr[i], arr[arr[i] - 1]
        swaps += 1

print(arr)
print(swaps)

#  Output Format

# Return the minimum number of swaps to sort the given array.

# Sample Input 0

# 4
# 4 3 1 2
# Sample Output 0

# 3