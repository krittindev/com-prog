def read_next(f):
    while True:
        t = f.readline()
        if len(t) == 0:       # ถ้าอ่านหมดแล้ว ออกจากวงวน
            break
        x = t.strip().split()  # ลบ blank ซ้ายขวา
        if len(x) == 2:       # แยกแล้วได้ 2 ส่วน --> ถูกต้อง ก็คืนผล
            return x[0], x[1]
    return "", ""             # แฟ้มหมดแล้ว คืนสตริงว่าง


def main():
    file_1, file_2 = (open(file_name) for file_name in input().strip().split())
    temp_id, temp_score = read_next(file_1)
    is_read_from_file_1 = True
    while True:
        current_id, current_score = '', ''

        if is_read_from_file_1:
            current_id, current_score = read_next(file_2)
        else:
            current_id, current_score = read_next(file_1)

        if temp_id == '' or current_id == '':
            if temp_id == '' and current_id == '':
                break
            elif temp_id == '':
                print(current_id, current_score)
            else:
                print(temp_id, temp_score)
                temp_id, temp_score = current_id, current_score
                is_read_from_file_1 = not is_read_from_file_1
            continue

        if temp_id[-2:] < current_id[-2:]:
            print(temp_id, temp_score)
            temp_id, temp_score = current_id, current_score
            is_read_from_file_1 = not is_read_from_file_1
        elif temp_id[-2:] == current_id[-2:]:
            if temp_id[:-2] < current_id[:-2]:
                print(temp_id, temp_score)
                temp_id, temp_score = current_id, current_score
                is_read_from_file_1 = not is_read_from_file_1
            else:
                print(current_id, current_score)
        else:
            print(current_id, current_score)


main()
