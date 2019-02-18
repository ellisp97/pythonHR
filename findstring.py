def count_substring(string, sub_string):
    count = 0
    for i in range(len(string)):
        check = False
        if sub_string[0] == string[i]:
            check = True
            j=0
            while check:
                try:
                    j += 1
                    if j == len(sub_string):
                        count += 1                   
                    if sub_string[j] != string[i+j]: 
                        check = False
                except:
                    check = False
                
    return count



if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)

    # edit soln


    # A = raw_input().strip()
    # x = raw_input().strip()

    # count = 0
    # for i in range(len(A) - len(x) + 1):
    #     if A[i:i+len(x)] == x:
    #         count += 1
    # print count