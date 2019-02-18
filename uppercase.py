# chris alan -> Chris Alan

firstName, surname = map(str, input().split())
firstSet = list(firstName)
secondSet = list(surname)
print("{}{} {}{}".format(firstSet[0].upper(),''.join(map(str, firstSet[1:])),secondSet[0].upper(),''.join(map(str, secondSet[1:]))))
