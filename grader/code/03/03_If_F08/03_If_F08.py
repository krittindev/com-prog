
def is_leap_year(y):
    result = False
    if y % 400 == 0:
        result = True
    if y % 4 == 0 and y % 100 != 0:
        result = True
    return result

def day_of_year(d, m, y):
    y -= 543
    days_of_months = [31, 29 if is_leap_year(y) else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    sum = 0
    for i in range(m):
        if i + 1 == m:
            sum += d
        else:
            sum += days_of_months[i]
    return sum
d, m, y = [int(input()) for _ in range(3)]
print(day_of_year(d, m, y))