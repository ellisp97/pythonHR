s1= input().strip()
s2= input().strip()
diff = {}
count = 0
for letter in s1:
    if letter not in diff:
        diff[letter] = 0
    diff[letter] += 1
    print(diff)
for letter in s2:
    if letter not in diff:
        diff[letter] = 0
    diff[letter] -= 1

print(sum(abs(n) for n in diff.values()))

