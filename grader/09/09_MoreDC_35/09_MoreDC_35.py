students = []

n = int(input().strip())

for _ in range(n):
    name, group, gen, department = input().strip().split()
    student = (name, group, gen, department)
    students.append(student)

keywords = input().strip().split()

search_result = []

for student in students:
    if set(keywords).issubset(set(student[1:])):
        search_result.append(student)

if len(search_result) == 0:
    print("Not Found")
else:
    for student in sorted(search_result):
        print(*student)
