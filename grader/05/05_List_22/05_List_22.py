def index_of(grades, ID):
    IDs = [e[0] for e in grades]
    if ID in IDs:
        return [e[0] for e in grades].index(ID)
    return -1

def upgrade(grades, IDs):
    indice = [index_of(grades, ID) for ID in IDs if index_of(grades, ID) != -1]
    grade_orders = ['A', "B+", 'B', "C+", 'C', "D+", 'D', 'F']
    for index in indice:
        if grades[index][1] != 'A':
            grade_orders_index = grade_orders.index(grades[index][1])
            grades[index][1] = grade_orders[grade_orders_index - 1]
    grades.sort()

grades = []
while True:
    t = input().strip()
    if t == 'q':
        break
    ID, grade = t.split()
    grades.append([ID, grade])
IDs = input().strip().split()
upgrade(grades, IDs)
for ID, grade in grades:
    print("{} {}".format(ID, grade))