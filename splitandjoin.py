def split_and_join(line):
    # write your code here
    words = list(map(str,line.split()))
    words = "-".join(words)
    return words

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)