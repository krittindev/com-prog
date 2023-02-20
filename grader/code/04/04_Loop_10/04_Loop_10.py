def get_bisection_log_10_2(a):
    c = 0
    temp_a = a
    while temp_a != 0:
        temp_a //= 10
        c += 1
    L = 0
    U = c
    x = (L + U) / 2
    while abs(a - 10**x) > 1e-10 * max(a, 10**x):
        if 10**x > a:
            U = x
        else:
            L = x
        x = (L + U) / 2
    return round(x, 6) # approximate 6 digits

def test():
    testcases = [1, 100, 100000000, 123456] # real number 1 -> 600
    solutions = [0.0, 2.0, 8.0, 5.091512]
    for i in range(len(testcases)):
        print("{:5} {:5} {:12}".format(\
            str(get_bisection_log_10_2(testcases[i])), \
            str(solutions[i]), \
            "✅" if get_bisection_log_10_2(testcases[i]) == solutions[i] else "❌" \
        ))

# test()
a = float(input()) # real number 1 -> 600
print(get_bisection_log_10_2(a))