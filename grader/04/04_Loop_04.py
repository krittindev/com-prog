def get_parentheses(text):
    result = ''
    for i in range(len(text)):
        if text[i] == '(':
            result += '['
        elif text[i] == '[':
            result += '('
        elif text[i] == ']':
            result += ')'
        elif text[i] == ')':
            result += ']'
        else:
            result += text[i]
    return result

def test():
    testcases = [
        "[[a + (b + [c / d] – e) + f] + 4]", 
        "no parentheses"
    ]
    solutions = [
        "((a + [b + (c / d) – e] + f) + 4)", 
        "no parentheses"
    ]
    for i in range(len(testcases)):
        testcase = get_parentheses(testcases[i])
        solution = solutions[i]
        print("{:5} {:5} {:12}".format(
            str(testcase),
            str(solution),
            "✅" if testcase == solution else "❌"
        ))

# test()
text = input()
print(get_parentheses(text))