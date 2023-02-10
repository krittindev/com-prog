import math

def is_leap_year(y):
    y -= 543
    result = False
    if y % 400 == 0:
        result = True
    if y % 4 == 0 and y % 100 != 0:
        result = True
    return result

def day_to_end_year(bd, bm, by):
    days_of_months = [31, 29 if is_leap_year(by) else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    days = sum(days_of_months[bm - 1:]) - bd + 1
    return days

def diff_year(by, y):
    return 365 * (y - by - 1) # when y >= by

def day_from_start_year(d, m, y):
    days_of_months = [31, 29 if is_leap_year(y) else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    days = sum(days_of_months[:m - 1]) + d - 1
    return days

bd, bm, by, d, m, y = [int(e) for e in input().split()]

total_day = day_to_end_year(bd, bm, by) + diff_year(by, y) + day_from_start_year(d, m, y)

physical = math.sin(2 * math.pi * total_day / 23)
emotional = math.sin(2 * math.pi * total_day / 28)
intellectual = math.sin(2 * math.pi * total_day / 33)

print( "{} {:.2f} {:.2f} {:.2f}".format(total_day, physical, emotional, intellectual))