def is_odd(n):
    # คืน (True/False) ว่า n เป็นจ านวนคี่หรือไม่
    return n % 2 != 0


def has_odds(x):
    # คืน (True/False) ว่า x เป็นลิสต์ที่มีข้อมูลบางตัวเป็นจ านวนคี่
    return any(is_odd(e) for e in x)


def all_odds(x):
    # คืน (True/False) ว่า x เป็นลิสต์ที่มีข้อมูลทุกตัวเป็นจ านวนคี่
    return all(is_odd(e) for e in x)


def no_odds(x):
    # คืน (True/False) ว่า x เป็นลิสต์ที่มีไม่มีข้อมูลที่เป็นจ านวนคี่เลย
    return all(not is_odd(e) for e in x)


def get_odds(x):
    # คืนลิสต์ที่มีจ านวนคี่ที่มีเก็บในลิสต์  x (ล าดับก่อนหลังให้เป็นไปตามล าดับเดียวกับใน x)
    # เช่น x = [1,2,3,5,0] จะได้ผลคือ [1,3,5]
    return [e for e in x if is_odd(e)]


def zip_odds(a, b):
    # คืนลิสต์ที่สร้างจากการน าจ านวนคี่ใน a และ b มาสลับกันเก็บในลิสต์ผลลัพธ์ (เริ่มจากใน a ก่อน)
    # เช่น a = [0,8,1,2,4,6,5,7,9,2,3] กับ b = [4,19,11,12,10,17] จะได้คือ
    # [1,19,5,11,7,17,9,3]
    filtered_a = get_odds(a)
    filtered_b = get_odds(b)
    result = []
    for i in range(max(len(filtered_a), len(filtered_b))):
        if i < len(filtered_a):
            result.append(filtered_a[i])
        if i < len(filtered_b):
            result.append(filtered_b[i])
    return result


exec(input().strip())  # ต้องมีค าสั่งนี้ ตรงนี้ ตอนส่งให้ Grader ตรวจ
