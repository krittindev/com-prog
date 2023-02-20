def str2RLE(t):
    l = []
    temp_c = ''
    sum = 0
    for e in t:
        if e == temp_c:
            sum += 1
        if e != temp_c:
            if sum != 0:
                l.append(temp_c)
                l.append(str(sum))
            temp_c = e
            sum = 1
    if sum != 0:
        l.append(temp_c)
        l.append(str(sum))
    return ' '.join(l)

def RLE2str(t):
    l = t.split()
    is_char = True
    s = ''
    for i in range(0, len(l), 2):
        s += l[i] * int(l[i + 1])
        is_char = not is_char
    return s

order = input()
if not (order == "str2RLE" or order == "RLE2str"):
    print("Error")
else:
    text = input()
    if order == "str2RLE":
        print(str2RLE(text))
    elif order == "RLE2str":
        print(RLE2str(text))

