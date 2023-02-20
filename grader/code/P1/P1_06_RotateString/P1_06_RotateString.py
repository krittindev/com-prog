operator = input()
n_lines = int(input())

s = ''
size = 0
for i in range(n_lines):
    line = input().strip()
    if i == 0:
        size = len(line)
    else:
        if not size == len(line):
            print("Invalid size")
            size = -1
            break
    s += line

if not size == -1:
    if operator == "90":
        for i in range(size):
            for j in range(n_lines):
                print(s[size * (n_lines - j - 1) + i], end = '')
            print()
    elif operator == "flip":
        for i in range(n_lines):
            for j in range(size):
                print(s[size * (i + 1) - j - 1], end = '')
            print()
    elif operator == "180":
        for i in range(n_lines):
            for j in range(size):
                print(s[size * (n_lines - i) - j - 1], end = '')
            print()
