import string

def print_rangoli(n):  
    # just a way of listing an alphabet
    # you can do list("abcd...") manually 
    alphabet = string.ascii_lowercase 
    L = []

    for i in range(n):
        s = "-".join(alphabet[i:n])
        L.append(s[::-1]+s[1:])
        # print(L)

    width = len(L[0])

    for i in range(n-1,0,-1):
        print(L[i].center(width,"-"))
    for i in range(n):
        print(L[i].center(width,"-"))

    return

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)