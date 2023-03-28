class Student:
    def __init__(self, line):
        id, gpax, com_prog_grade, cal1_grade, cal2_grade = line.split()
        self.id = id
        self.gpax = float(gpax)
        self.com_prog_grade = com_prog_grade
        self.cal1_grade = cal1_grade
        self.cal2_grade = cal2_grade

    def is_grade_pass(self):
        return self.com_prog_grade == 'A' and self.cal1_grade <= 'C' and self.cal2_grade <= 'C'


def select_students(a, b):
    if not a.is_grade_pass() and not b.is_grade_pass():
        print("None")
    elif a.is_grade_pass() and not b.is_grade_pass():
        print(a.id)
    elif not a.is_grade_pass() and b.is_grade_pass():
        print(b.id)
    else:
        if a.gpax > b.gpax:
            print(a.id)
        elif a.gpax < b.gpax:
            print(b.id)
        else:
            if a.cal1_grade < b.cal1_grade:
                print(a.id)
            elif a.cal1_grade > b.cal1_grade:
                print(b.id)
            else:
                if a.cal2_grade < b.cal2_grade:
                    print(a.id)
                elif a.cal2_grade > b.cal2_grade:
                    print(b.id)
                else:
                    print("Both")

def test():
    test_cases = [
        [
            "7039999921 2.8 B C C",
            "7030000021 3.5 B A A"
        ],
        [
            "7039999921 2.8 A C C",
            "7030000021 3.5 B A A"
        ],
        [
            "7030000021 3.2 A A D",
            "7039999921 2.8 A C C"
        ],
        [
            "7039999921 3.1 A B B",
            "7030000021 3.0 A A A"
        ],
        [
            "7039999921 3.1 A B B",
            "7030000021 3.1 A C A"
        ],
        [
            "7039999921 3.1 A C A",
            "7030000021 3.1 A C C"
        ],
        [
            "7039999921 3.1 A C B",
            "7030000021 3.1 A C B"
        ]
    ]
    for test_case in test_cases:
        a, b = [Student(line) for line in test_case]
        select_students(a, b)


# test()
a, b = Student(input()), Student(input())
select_students(a, b)
