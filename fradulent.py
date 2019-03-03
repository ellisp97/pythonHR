# the amount spent by a client on a particular day is greater than or equal to  the client's
# median spending for a trailing number of days, they send the client a notification about potential fraud. 
# def median(lst):
#     n = len(lst)
#     if n < 1:
#             return None
#     if n % 2 == 1:
#             return sorted(lst)[n//2]
#     else:
#             return sum(sorted(lst)[n//2-1:n//2+1])/2.0


# noDays, noTrailDays = map(int, input().split())
# expenditure = list(map(int, input().split()))

# For example, d=3 and expenditures=[10,20,30,40,50] .On the first three days, they just collect spending data. At day 4, we have trailing expenditures of [10,20,30]
# The median is 20 and the day's expenditure is 40 Because 40>= 2*20, there will be a notice. The next day, our trailing expenditures are [20,30.40] and the expenditures are 50.
# This is less 2*30 than  so no notice will be sent. Over the period, there was one notice sent.

# first figure out median using defined function above

# noticecount = 0
# for i in range(noDays-noTrailDays):
#     medEle = median(expenditure[i:i+noTrailDays])
#     currExp = expenditure[noTrailDays+i]
#     if currExp >= 2*medEle:
#         noticecount += 1

# print(noticecount)


# =====================THE ABOVE FUNCTION SORTS THE ARRAY ON EVERY RUN=========================
# THIS SEG FAULTS FOR LARGE CASES, SIMPLY DECREASE OLD VALUE FROM COUNT SORT AND ADD NEW ONE O(1)
# THIS METHOS USES A COUTNING SORT O(N), AS WE KNOW 1 <= Expenditure <= 200, AS WE'RE KICKING OUT A VALUE
# EVERY TIME WE CAN USE A QUEUE - USEFUL AS THE SPACE NEEDED TO STORE 200 INDEXES IS LOW


def get_median(counting_sort_list,trailing_days,median_pos):
    counter, left = 0, 0
    # find number where we pass through median
    while counter<median_pos:
        counter += counting_sort_list[left]
        left +=1

    # step back one time - pass through median to take step back to left position
    right = left
    left -= 1

    # if odd, or both left and right number are the same
    if counter > median_pos or trailing_days %2  !=0:
        return left
    else:
        # find value for even
        while counting_sort_list[right] == 0:
            right += 1
        return (left + right)/2
def activityNotifications(expenditure, trailing_days):
    counting_sort_list = [0]*201
    end = trailing_days

    # perform counting sort
    for i in range(end):
        counting_sort_list[expenditure[i]] += 1

    current = 0
    total_notifications = 0

    # determine odd or even median position
    if trailing_days % 2 ==0:
        median_pos = int(trailing_days/2)
    else:
        median_pos = int(trailing_days/2) + 1

    total_expenditure_length = len(expenditure)

    # start and move along expenditure list
    while end < total_expenditure_length:
        median = get_median(counting_sort_list,trailing_days,median_pos)
        if expenditure[end] >= median*2:
            total_notifications +=1

        # modify the queue FIFO
        counting_sort_list[expenditure[current]] -= 1
        counting_sort_list[expenditure[end]] += 1
        current += 1
        end += 1

    return total_notifications


if __name__ == '__main__':
    n, d = map(int, input().split())
    expenditure = list(map(int, input().rstrip().split()))

    result = activityNotifications(expenditure, d)
    print(result)