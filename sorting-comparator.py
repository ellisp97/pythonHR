from functools import cmp_to_key

class Player:
    def __init__(self,name,score):
        self.name = name
        self.score = score

    def comparator(a,b):
        if a.score < b.score:
            return -1
        elif a.score > b.score:
            return 1
        else: 
            if a.name < b.name:
                return 1
            else:
                return -1


n = int(input())
L = []
for i in range(n):
    name,score = input().split()
    player = Player(name, int(score))
    L.append(player)

data = sorted(L, key=cmp_to_key(Player.comparator))
for i in data:
    print(i.name, i.score)


# playerr class - name string score integer
# Sample Input

# 5
# amy 100
# david 100
# heraldo 50
# aakansha 75
# aleksa 150
# Sample Output

# aleksa 150
# amy 100
# david 100
# aakansha 75
# heraldo 50
# Explanation

# As you can see, the players are first sorted by decreasing score and then sorted alphabetically by name.
