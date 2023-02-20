def next_15_days(d, m, y):
    m30 = [4, 6, 9, 11]
    y -= 543
    n = 31
    if m in m30:
        n = 30
    else:
        if m == 2:
            n = 28
            if y % 400 == 0:
                n = 29
            if y % 4 == 0 and y % 100 != 0:
                n = 29
    d += 15
    if d > n:
        d -= n
        m += 1
    if m > 12:
        m -= 12
        y += 1
    y += 543
    return d, m, y

def test():
    test_cases = ["1 1 2560", "31 12 2560", "28 2 2559", "28 2 2560"]
    for test_case in test_cases:
        d, m, y = [int(e) for e in test_case.split()]
        print('/'.join(str(e) for e in next_15_days(d, m, y)))

# test()
d, m, y = [int(e) for e in input().split()]
print('/'.join(str(e) for e in next_15_days(d, m, y)))