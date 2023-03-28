def read_date():
    month_names = ["Jan", "Feb", "Mar", "Apr",
                   "May", "Jun", "Jul", "Aug",
                   "Sep", "Oct", "Nov", "Dec"]
    date = input().split()
    d = int(date[0])
    m = month_names.index(date[1][:3]) + 1
    y = int(date[2])
    return [d, m, y]


def zodiac(d, m):
    zodiac_names = ["Aries", "Taurus", "Gemini", "Cancer", "Leo", "Virgo",
                    "Libra", "Scorpio", "Sagittarius", "Capricorn", "Aquarius", "Pisces"]
    zodiac_name = zodiac_names[(m - 3 - (1 if d < 21 else 0)) % 12]
    return zodiac_name


def days_in_feb(y):
    d = 28
    if y % 400 == 0 or y % 100 != 0 and y % 4 == 0:
        d = 29
    return d


def days_in_month(m, y):
    day_of_months = [31, days_in_feb(
        y), 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    return day_of_months[m - 1]


def days_in_between(d1, m1, y1, d2, m2, y2):
    days = sum(days_in_month(m, y1) for m in range(12, 1, -1) if m1 < m)
    days += sum(days_in_month(m, y2) for m in range(1, 12) if m2 > m)
    days += (days_in_month(m1, y1) - d1 + 1) + \
        int((y2 - y1 - 1)*365.25) + (d2 - 1)
    return days


def main():
    d1, m1, y1 = read_date()
    d2, m2, y2 = read_date()
    print(zodiac(d1, m1), zodiac(d2, m2))
    print(days_in_between(d1, m1, y1, d2, m2, y2))


exec(input().strip())
