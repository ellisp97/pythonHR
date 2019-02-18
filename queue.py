

# notests = int(input())
# queuesize = [0]*notests
# queue = [0]*notests
# normalQ = [0]*notests

# for i in range(notests):
#     queuesize[i] = int(input())
#     normalQ[i] = [i+1 for i in range(queuesize[i])]
#     queue[i] = list(map(int, input().split()))

# for j in range(notests):
#     for i in range(queuesize[j]):
#         print("this is element {} in array {}".format(queue[j][i], i))
#         if int(queue[j][i]) < int(i-3) or int(queue[j][i]) > int(i+3): 
#             print("Chaotic")
#             break
#         # elif not queue[j][i] == normalQ[j][i]:
#         #     if queue[j][i]) <= int(i-3) or int(queue[j][i]) > int(i+3)


# =================ANSWER==================
t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    org = list(range(n+1))
    pos = list(range(n+1))
    cnt = [0]*(n + 1)
    ans = 0
    invalid = 0

    for i in range(n - 1, -1, -1):
    
            if invalid:
                break
            # Get position where arr[i] should have been if no one bribed after this point
            oldp = pos[arr[i]]
            # Get the position where arr[i] currently is.
            newp = i + 1
            # oldp != newp indicates that even after this point, bribes took place
            # counting the number of furthter bribes that took place to bring arr[i] to i
            while oldp != newp:
                ans = ans + 1
                # arr[i] is at the right of org[oldp + 1] in the given array
                # that means org[oldp + 1] bribed arr[i] at some point
                # so increasing its count by 1

                cnt[org[oldp + 1]] += 1
                # print("org[oldp +1] {} on position oldp+1 {} must have bribed arr[i] {} at some point count {}".format(org[oldp + 1],oldp+1,arr[i],cnt[org[oldp + 1]]))

                if cnt[org[oldp + 1]] > 2:
                    invalid = 1
                    break

                # updating the original array to match the array after this bribe took place
                org[oldp], org[oldp+1] = org[oldp+1], org[oldp]

                # update the positions also due to the change 
                # caused by bribe that took place so far
                
                pos[org[oldp]] = oldp
                pos[org[oldp + 1]] = oldp + 1
                
                oldp = oldp + 1

    if invalid:
            ans = "Too chaotic"
    print(ans)
# Output Format

# Print an integer denoting the minimum number of bribes needed to get the queue into its final state. Print Too chaotic if the state is invalid, i.e. it requires a person to have bribed more than  people.

# Sample Input

# 2
# 5
# 2 1 5 3 4
# 5
# 2 5 1 3 4
# Sample Output

# 3
# Too chaotic