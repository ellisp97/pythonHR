

def is_matched(expression):
    mapping = dict(zip('({[', ')}]'))
    queue = []
    for letter in expression:
        print(letter)
        if letter in mapping:
            queue.append(mapping[letter])
            print(queue)
        elif not (queue and letter == queue.pop()):
            return False
    return not queue


n = int(input())
for i in range(n):
    s = list(input().strip())
    if is_matched(s):
        print('YES')
    else:
        print('NO')
