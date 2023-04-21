def get_dept(depts_selected, dept_requires):
    for dept in depts_selected:
        if dept_requires[dept] > 0:
            return dept

    raise Exception("Student has no dept")


def main():
    n_depts = int(input().strip())
    dept_requires = {}

    for _ in range(n_depts):
        dept, _require = input().strip().split()
        require = int(_require)
        dept_requires[dept] = require

    n_students = int(input().strip())
    students_unsorted = []
    students_sorted_by_score = []
    students_dept_selected = []

    for _ in range(n_students):
        student_id, _score, *depts_selected = input().strip().split()
        score = float(_score)
        students_unsorted.append(
            (-score, student_id, tuple(depts_selected)))

    for student in sorted(students_unsorted):
        score, student_id, depts_selected = student
        students_sorted_by_score.append(
            (student_id, -score, depts_selected))

    for student in students_sorted_by_score:
        student_id, score, depts_selected = student
        dept = get_dept(depts_selected, dept_requires)
        dept_requires[dept] -= 1
        students_dept_selected.append((student_id, dept))

    for student in sorted(students_dept_selected):
        student_id, dept = student
        print(student_id, dept)


main()
