# -*- coding: iso-8859-15 -*-
# HW3_List_processing_Function (ไม่ลบหรือแก้ไขบรรทัดนี้ หรือเพิ่มอะไรก่อนบรรทัดนี้ โดยเด็ดขาด)

# - เขียนในเซลล์นี้เท่านั้น 
# - ถ้าต้องการเขียนฟังก์ชันเพิ่ม ก็เขียนในเซลล์นี้

def get_weighted_score(weights, grades):
    sum = 0 # init SUM = 0
    grade_alpa = ['F','D','C','B','A'] # F = 0, D = 1 , ...
    for index in range(len(weights)): # index -> 0, 1, 2, 3 ... < length of Weights list
        sum += weights[index] * grade_alpa.index(grades[index]) # weights * index of grade alphabet list
    return sum 

# ---------------------------------------------------
def student_sorting(stu_weight_scores, n):
    if len(stu_weight_scores) == 0 or n == 0:
        return [] # 0 safty
    result = []
    nest_list = []
    for i in range(0, len(stu_weight_scores), 2): # loop 0, 2, 4, ... < legth of stu_weight_scores for stu
        nest_list.append([stu_weight_scores[i + 1], stu_weight_scores[i]]) # make [ [24 , 'sdf'] , [64 , 'grb'] , ... ]
    sorted_nest_list = sorted(nest_list, reverse = True) # sort reversed
    for i in range(n):
        result.append(sorted_nest_list[i][1])
    return result

# ---------------------------------------------------
def test():
    # ตัวตรวจจะไม่สนใจการทำงานใดๆใน ฟังก์ชันนี้ นิสิตสามารถเพิ่มโค้ดในนี้เพื่อทดสอบฟังก์ชัน
    # ที่เขียนมาข้างบนได้

    # ตัวอย่างการเขียนโค้ดทดสอบฟังก์ชัน get_weighted_score
    my_weighted_score = get_weighted_score([1,1,9,1,1,1,1], 'AABAAAA')
    print(my_weighted_score)

    # ตัวอย่างการเขียนโค้ดทดสอบฟังก์ชัน student_sorting
    S = ["stu04",48,"stu10",52,"stu22",40,"stu19",35,"stu23",44,"stu07",59,"stu40",57,"stu05",36]
    n_stu = 5
    selected_students = student_sorting(S, n_stu)
    print(selected_students)

test()