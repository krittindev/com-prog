def reverse(d):
    # d เป็น dict ที่มี value ไม่ซ ้ํากัน
    # คืน dict ใหม่ที่เก็บ key,value ที่ค่ําเป็น value,key ของ d ที่ได้รับ
    reversed_dict = {}
    for key, value in d.items():
      reversed_dict[value] = key
    return reversed_dict


def keys(d, v):
    # คืนลิสต์ที่เก็บค่ําของ keys ใน d (เรียงยังไงก็ได้) ที่มีค่ํา value เท่ํากับ v
    list_key = []
    for key, value in d.items():
      if value == v:
        list_key.append(key)
    return list_key

exec(input().strip())    # ต้องมีค ําสั่งนี้ ตรงนี้ ตอนส่งให้ Grader ตรวจ