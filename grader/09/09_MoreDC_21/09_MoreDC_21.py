def factor(N):
    _factor = {}
    divider = 2
    while N != 1:
        if N % divider == 0:
            while N % divider == 0:
                N //= divider
                if divider in _factor:
                    _factor[divider] += 1
                else:
                    _factor[divider] = 1
        divider += 1
    _factor = [[divider, power] for divider, power in _factor.items()]
    _factor.sort()
    return _factor


exec(input().strip())  # ตอ้ งมคี ําส่ังนี้ ตรงนี้ ตอนสง่ ให้Grader ตรวจ
