n = int(input())

students = []
for _ in range(n):
    students.append(list(map(str, input().split())))

students = sorted(students, key = lambda x : int(x[i]))

for i in students:
    print(i[0], end = ' ')