def icecream(money,sizeArr,costs):
    if len(costs) <= 1:
        return False
    buff_dict = {}
    for i in range(sizeArr):
        if costs[i] in buff_dict:
            return [buff_dict[costs[i]], i]
        else:
            buff_dict[money - costs[i]] = i
        print(buff_dict)



if __name__ == '__main__':
    noTrips = int(input())
    for i in range(noTrips):
        money = int(input())
        sizeArr = int(input())
        costs = list(map(int,input().split()))
        result = icecream(money,sizeArr,costs)
        print(result)




# Sample Input

# 2
# 4
# 5
# 1 4 5 3 2
# 4
# 4
# 2 2 4 3
# Sample Output

# 1 4
# 1 2
# Explanation

# Sunny and Johnny make the following two trips to the parlor:

# The first time, they pool together money=4 dollars. 
# There are five flavors available that day and flavors 1 and 4 have a total cost of 1+3=4.
# The second time, they pool together money=4 dollars. 
# There are four flavors available that day and flavors 1 and 2 have a total cost of 2+2=4.