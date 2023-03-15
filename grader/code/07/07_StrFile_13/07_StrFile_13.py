def isAlphaNumerical(c):
    if '0' <= c <= '9' or 'A' <= c <= 'Z' or 'a' <= c <= 'z':
        return True
    return False


def isAlphabet(c):
    if 'A' <= c <= 'Z' or 'a' <= c <= 'z':
        return True
    return False


def cleanUp(text):
    newText = ''
    for c in text:
        if isAlphaNumerical(c):
            newText += c.lower()
        else:
            newText += ' '
    return newText


def camelCase(texts):
    camelCasedText = ''
    for text in texts:
        if camelCasedText == '':
            camelCasedText += text
        else:
            camelCasedText += text[0].upper() + text[1:]
    return camelCasedText


line = input()
cleanedLine = cleanUp(line)
listText = cleanedLine.split()
print(camelCase(listText))
