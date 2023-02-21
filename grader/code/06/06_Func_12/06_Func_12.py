def is_prime(n):
    # ทดสอบว่า n เป็นจ านวนเฉพาะหรือไม่
    if n <= 1:
        return False
    for k in range(2, int(n**0.5)+1):
        if n % k == 0:
            return False
    return True


def next_prime(N):
    # คืนจ านวนเฉพาะตัวที่มีค่าน้อยสุดที่มากกว่า N
    while True:
        N += 1
        if is_prime(N):
            return N


def next_twin_prime(N):
    # คืนจ านวนเฉพาะสองค่าที่เป็น twin prime ที่มีค่าน้อยสุดที่มากกว่า N
    # twin prime คือจ านวนเฉพาะที่มีค่าต่างกัน 2  เช่น 11 กับ 13 หรือ 41 กับ 43
    while True:
        N += 1
        if is_prime(N) and is_prime(N + 2):
            return N, N + 2


exec(input().strip())    # ต้องมีค าสั่งนี้ ตรงนี้ ตอนส่งให้ Grader ตรวจ
