
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
# print( day_of_year(1, 1, 2559) )
# print( day_of_year(31, 12, 2559) )
# print( day_of_year(5, 12, 2560) )
# print( day_of_year(31, 12, 2560) )
exec(input()) # DON'T remove this line