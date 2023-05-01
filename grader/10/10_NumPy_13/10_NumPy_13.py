import numpy as np


def p(X):
    # X เป็นอาเรย์ขนาด n2 เก็บจ านวนโจทย์ที่ท า (คอลัมน์ 0) กับเกรดเฉลี่ย (คอลัมน์ 1) ของนักเรียน n คน
    # คืนอาเรย์ขนาด n ช่อง เก็บความน่าจะเป็นที่นักเรียนแต่ละคนจะเรียนผ่านวิชา ค านวณจากสูตรข้างบน
    # ใช้ความสามารถของ NumPy จะเขียนได้โดยไม่ต้องใช้วงวน (อย่างมาก 3 บรรทัด)
    logit = -3.98 + 0.1 * X[:, 0] + 0.5 * X[:, 1]
    return 1 / (1 + np.e ** -logit)


exec(input().strip())    # ต้องมีค าสั่งนี้ ตรงนี้ ตอนส่งให้ Grader ตรวจ
