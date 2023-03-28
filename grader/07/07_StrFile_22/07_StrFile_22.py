def isAnagram(text1, text2):
    text1 = sorted(text1.replace(' ', '').lower())
    text2 = sorted(text2.replace(' ', '').lower())
    if text1 == text2:
        return True
    return False


line1, line2 = input(), input()

if isAnagram(line1, line2):
    print('YES')
else:
    print('NO')
