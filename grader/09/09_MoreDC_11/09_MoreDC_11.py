n = int(input().strip())

for _ in range(n):
    line = input()
    is_not_pass = True
    len_space = 0
    for e in line:
        if e != ".":
            break
        len_space += 1
    print("{}{}".format("." * (len_space // 2), line[len_space:]))
