def get_mcq(solution, answer):
    if len(solution) != len(answer):
        return "Incomplete answer"
    score = sum([1 if solution[i] == answer[i]
                else 0 for i in range(len(solution))])
    return score


def test():
    testcases = [
        [
            "AAABC",
            "AABCC"
        ],
        [
            "AAAAAAAAAAAAAAAAAAAAAAA",
            "BBBXXBBBBB BBBBB BBBBBB"
        ],
        [
            "AAAAAAAAAAAAAAAAAAAAAAAAAAAAA",
            "AAAAAAAAAAAA"
        ]
    ]
    solutions = [
        3,
        0,
        "Incomplete answer"
    ]
    for i in range(len(testcases)):
        testcase = get_mcq(testcases[i][0], testcases[i][1])
        solution = solutions[i]
        print("{:5} {:5} {:12}".format(
            str(testcase),
            str(solution),
            "✅" if testcase == solution else "❌"
        ))

# test()
solution, answer = input(), input()
print(get_mcq(solution, answer))