def get_birthday_paradox(p):
    k = 1
    t = 1
    while True:
        t = (t * (365 - (k - 1))) / 365
        if not 1 - t >= p:
            k += 1
        else:
            return k

def test():
    testcases = [0.0, 0.7]
    solutions = [1, 30]
    for i in range(len(testcases)):
        print("{:5} {:5} {:12}".format(\
            get_birthday_paradox(testcases[i]), \
            solutions[i], \
            "✅" if get_birthday_paradox(testcases[i]) == solutions[i] else "❌" \
        ))
# test()
print(get_birthday_paradox(float(input())))