def faculty_code(id):
    ids = ["01", "02", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31", "32", "33", "34", "35", "36", "37", "38", "39", "40", "51", "53", "55", "58"]
    return id in ids

def test():
    test_cases = ["Engineering", "1", "10", "20000", "58", "01"]
    for id in test_cases:
        print("OK" if faculty_code(id) else "Error")

test()
# id = input()
# print("OK" if faculty_code(id) else "Error")