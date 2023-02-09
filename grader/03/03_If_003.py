def flowchart_01(a, b, c, d):
    if a > b:
        a, b = b, a
        if d >= a:
            if c > d:
                c -= a
        else:
            c += a
        b = a + c + d
    else:
        if c > a >= b:
            d += a
        if d > c:
            b += 2
        else:
            b *= 2
    return a, b, c, d

def test():
    test_cases = ["1 2 3 4", "4 3 2 1", "2 2 2 2", "9 0 9 0", "3 2 1 4"]
    for test_case in test_cases:
        a, b, c, d = [int(e) for e in test_case.split()]
        print(' '.join(str(e) for e in flowchart_01(a, b, c, d)))

test()
# a, b, c, d = [int(e) for e in input().split()]
# print(' '.join(str(e) for e in flowchart_01(a, b, c, d)))
