def rot13Line(line):
    rotatedLine = ''

    for c in line:
        if 'A' <= c <= 'M' or 'a' <= c <= 'm':
            rotatedLine += chr(ord(c) + 13)
        elif 'N' <= c <= 'Z' or 'n' <= c <= 'z':
            rotatedLine += chr(ord(c) - 13)
        else:
            rotatedLine += c

    return rotatedLine


while True:
    line = input()

    if line == 'end':
        break

    rotatedLine = rot13Line(line)
    print(rotatedLine)
