def get_bisection_log_10(a):
    L = 0
    U = a
    x = (L + U) / 2
    while abs(a - 10**x) > 1e-10 * max(a, 10**x):
        if 10**x > a:
            U = x
        else:
            L = x
        x = (L + U) / 2
    return round(x, 6) # approximate 6 digits

def test():
    testcases = [1.0, 100.0, 250.0, 500.0] # real number 1 -> 600
    solutions = [0.0, 2.0, 2.39794, 2.69897]
    for i in range(len(testcases)):
        print("{:5} {:5} {:12}".format(\
            str(get_bisection_log_10(testcases[i])), \
            str(solutions[i]), \
            "✅" if get_bisection_log_10(testcases[i]) == solutions[i] else "❌" \
        ))

# test()
a = float(input()) # real number 1 -> 600
print(get_bisection_log_10(a))