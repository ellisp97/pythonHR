def minion_game(string):
    # make substrings of s
    # Stuart can only start with constnants
    # Kevin Vowels
    vowels = set("AEIOU")
    # consonants = set("bcdfghjklmnpqrstvwxyz")
    Stuart = 0
    Kevin = 0
    for i in range(len(string)):
        if string[i] in vowels:
            Kevin += (len(string) - i)
        else: 
            Stuart += (len(string) - i)

    if Kevin > Stuart:
            print ("Kevin", Kevin)
    elif Kevin < Stuart:
        print ("Stuart", Stuart)
    else:
        print ("Draw")

if __name__ == '__main__':
    s = input()
    minion_game(s)