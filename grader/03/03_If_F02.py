class Student:
    def __init__(self, id, gpax, com_prog_grade, cal1_grade, cal2_grade):
        self.id = id
        self.gpax = float(gpax)
        self.com_prog_grade = com_prog_grade
        self.cal1_grade = cal1_grade
        self.cal2_grade = cal2_grade

    def is_grade_pass(self):
        return self.com_prog_grade == 'A' and self.cal1_grade <= 'C' and self.cal2_grade <= 'C'

    def description(self):
        return ' '.join([self.id, str(self.gpax), self.com_prog_grade, self.cal1_grade, self.cal2_grade])

def choose(stu1, stu2): 
    stu1_id, stu1_gpax, stu1_com_prog_grade, stu1_cal1_grade, stu1_cal2_grade = stu1
    stu2_id, stu2_gpax, stu2_com_prog_grade, stu2_cal1_grade, stu2_cal2_grade = stu2
    a = Student(stu1_id, stu1_gpax, stu1_com_prog_grade, stu1_cal1_grade, stu1_cal2_grade)
    b = Student(stu2_id, stu2_gpax, stu2_com_prog_grade, stu2_cal1_grade, stu2_cal2_grade)
    # print(a.description(), b.description())
    if not a.is_grade_pass() and not b.is_grade_pass():
        return []
    elif a.is_grade_pass() and not b.is_grade_pass():
        return [a.id]
    elif not a.is_grade_pass() and b.is_grade_pass():
        return [b.id]
    else:
        if a.gpax > b.gpax:
            return [a.id]
        elif a.gpax < b.gpax:
            return [b.id]
        else:
            if a.cal1_grade < b.cal1_grade:
                return [a.id]
            elif a.cal1_grade > b.cal1_grade:
                return [b.id]
            else:
                if a.cal2_grade < b.cal2_grade:
                    return [a.id]
                elif a.cal2_grade > b.cal2_grade:
                    return [b.id]
                else:
                    return [a.id, b.id]

# print( choose(['7039999921',2.8,'B','C','C'], ['7030000021',3.5,'A','A','D']) )
# print( choose(['7039999921',2.8,'A','C','C'], ['7030000021',3.5,'B','A','A']) )
# print( choose(['7030000021',3.5,'A','A','D'], ['7039999921',2.8,'A','C','C']) )
# print( choose(['7039999921',2.8,'A','C','C'], ['7030000021',2.7,'A','A','A']) )
# print( choose(['7039999921',3.5,'A','B','B'], ['7030000021',3.5,'A','C','A']) )
# print( choose(['7039999921',3.5,'A','B','B'], ['7030000021',3.5,'A','B','C']) )
# print( choose(['7039999921',3.5,'A','B','A'], ['7030000021',3.5,'A','B','A']) )
exec(input()) # DON'T remove this line