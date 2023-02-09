def get_count_word(word, text):
    words = ''.join(e if e not in "\"(),.'" else ' ' for e in text).split()
    return words.count(word)

def test():
    testcases = [
        [
            "the",
            "The word \"the\" is one of the most common words in English."
        ],
        [
            "Sadet",
            "\"Phra Sadet\" tham \"Phra Sadet\" wa ja sadet rue mai sadet."
        ],
        [
            "ABC",
            "(\"ABC aABC AABC ABCAB CABC d ABC k abc ABC\" kjdk abc asd 'ABC ajdsABCkjas  ABC' ABC abc ABC ABC ABC ABCABC...ABC"
        ]
    ]
    solutions = [
        2,
        2,
        10
    ]
    for i in range(len(testcases)):
        testcase = get_count_word(testcases[i][0], testcases[i][1])
        solution = solutions[i]
        print("{:5} {:5} {:12}".format(
            str(testcase),
            str(solution),
            "✅" if testcase == solution else "❌"
        ))

test()
# word, text = input(), input()
# print(get_count_word(word, text))