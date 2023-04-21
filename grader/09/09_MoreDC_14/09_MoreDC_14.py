courses_file = open(input().strip(), 'r')
teachers_file = open(input().strip(), 'r')
database_file = open(input().strip(), 'r')

courses = {}
teachers = {}
database = []

for line in courses_file:
    key, value = line.strip().split(',')
    courses[key] = value

for line in teachers_file:
    key, value = line.strip().split(',')
    teachers[key] = value

for line in database_file:
    key_course, key_teacher = line.strip().split(',')
    database.append((key_course, key_teacher))

for key_course, key_teacher in database:
    if key_course not in courses or key_teacher not in teachers:
        print('record error')
        continue

    print(','.join([courses[key_course], teachers[key_teacher]]))

courses_file.close()
teachers_file.close()
database_file.close()
