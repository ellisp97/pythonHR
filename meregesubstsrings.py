# DOESNT WORK FOR ALL TEST CASES
# def merge_the_tools(s,k):
#     noLines = len(s)/k
#     kArrays = []
#     for i in range(0,len(s),3):
#         kArrays.append(s[i:i+3])
#     # remove any non distinct letters
#     uniqueLetters =[0 for x in range(int(noLines))]

#     for i in range(len(kArrays)):
#         uniqueLetters[i] = []
#         for j in range(len(kArrays[i])):
#             if not (kArrays[i][j] in uniqueLetters[i]):
#                 uniqueLetters[i].append(kArrays[i][j])

#     for i in range(int(noLines)):    
#         print(''.join(uniqueLetters[i]))
#     return
    




def merge_the_tools(S,K):
    temp = []
    len_temp = 0
    for item in S:
        len_temp += 1
        if item not in temp:
            temp.append(item)
        if len_temp == K:
            print (''.join(temp))
            temp = []
            len_temp = 0
    return

string, k = input(), int(input())
merge_the_tools(string, k)

# Sample Input

# AABCAAADA
# 3   
# Sample Output

# AB
# CA
# AD