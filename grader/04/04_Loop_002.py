def get_partition(d):
    p = d[-1]
    i = -1; j = 0
    n = len(d)
    while j < n - 1:
        if d[j] <= p:
            i += 1
            d[i], d[j] = d[j], d[i]
        j += 1
    d[i + 1], d[-1] = d[-1], d[i + 1]
    return d

def test():
    testcases = [[1, 2, 3, 4, 5], [5, 4, 3, 2, 1], [9, 2, 7, 1, 6, 8, 4, 5]]
    solutions = [[1, 2, 3, 4, 5], [1, 4, 3, 2, 5], [2, 1, 4, 5, 6, 8, 7, 9]]
    for i in range(len(testcases)):
        print("{:5} {:5} {:12}".format(\
            str(get_partition(testcases[i])), \
            str(solutions[i]), \
            "✅" if get_partition(testcases[i]) == solutions[i] else "❌" \
        ))
# test()
d = [int(e) for e in input().split()]
print(get_partition(d))