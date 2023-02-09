import math

def sqrt_n_times(x, n): 
    # คืนน่าที่เสมือนการนำค่าใน x มากดปุ่ม sqrt เป็นจำนวน n ครั้ง
    if n == 1:
        return math.sqrt(x)
    return math.sqrt(sqrt_n_times(x, n - 1))
    
def cube_root(y):
    # คืนค่าประมาณของรากที่สามของ y โดยใช้วิธีที่เสมือนการกดปุ่มด้วยสูตร
    # y^(1/2^2)(1+1/2^2)(1+1/2^4)(1+1/2^8)(1+1/2^16)(1+1/2^32)
    # ข้อแนะนำ : เรียกใช้ฟังก์ชัน sqrt_n_times
    y = sqrt_n_times(y, 2)
    y *= sqrt_n_times(y, 2)
    y *= sqrt_n_times(y, 4)
    y *= sqrt_n_times(y, 8)
    y *= sqrt_n_times(y, 16)
    y *= sqrt_n_times(y, 32)
    return y
    
def main():
    q = float(input()) 
    print(cube_root(q))
    
exec(input()) # DON'T remove this line