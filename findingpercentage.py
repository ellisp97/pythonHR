n = int(input())
student_marks = []
for _ in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks.append([name,scores])
query_name = input()

# print(student_marks)
# print(student_marks[0][0])
for i in range(n):
    if student_marks[i][0] == query_name:
        avg = student_marks[i][1]

print("%.2f" % (sum(avg)/float(len(avg))))

# print(avgscore)

# Way better answer using dictionaries
d={}
for i in range(int(input())):
    line=input().split()
    d[line[0]]=sum(map(float,line[1:]))/3

print ('%.2f' % d[input()])

# 3
# Krishna 67 68 69
# Arjun 70 98 63
# Malika 52 56 60
# Malika