def get_rle(text):
    l = [text[0]]
    temp_c = text[0]
    sum = 1
    for e in text[1:]:
        if e == temp_c:
            sum += 1
        if e != temp_c:
            l.append(sum)
            l.append(e)
            temp_c = e
            sum = 1
    l.append(sum)
    return ' '.join([str(e) for e in l])

def test():
    testcases = ["zzzZZZZZZZZZZZZZZZZZZZZZZZZZZ", "ABBA"]
    solutions = ["z 3 Z 26", "A 1 B 2 A 1"]
    for i in range(len(testcases)):
        print("{:5} {:5} {:12}".format(\
            str(get_rle(testcases[i])), \
            str(solutions[i]), \
            "✅" if get_rle(testcases[i]) == solutions[i] else "❌" \
        ))

# test()
text = input()
print(get_rle(text))