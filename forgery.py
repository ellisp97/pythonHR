#===========  𝑂(𝑁*𝑀) ===============
from collections import Counter


# canUse = True
# for word in note:
#     if not word in magazine:
#         canUse = False
#     else: 
#         magazine.remove(word)

# print(canUse)

# check the hash in 𝑂(1) time for a result of 𝑂(𝑁) to construct the hash and 𝑂(𝑀) to check all m words, which is a final 𝑂(𝑁+𝑀).

def ransom_note(magazine, ransom):
    print(magazine)
    print(ransom)
    word_counts = Counter(magazine)
    for word in ransom:
        print(word_counts[word])
        if word_counts[word] > 0:
            word_counts[word] -= 1
        else:
            return False
    return True

n,m = map(int, input().split())
magazine= input().strip().split()
ransom=  input().strip().split()
answer = ransom_note(magazine, ransom)


#  Sample Input 0

# 6 4
# give me one grand today night
# give one grand today
# Sample Output 0

# Yes
# Sample Input 1

# 6 5
# two times three is not four
# two times two is four
# Sample Output 1

# No
# Explanation 1

# 'two' only occurs once in the magazine.