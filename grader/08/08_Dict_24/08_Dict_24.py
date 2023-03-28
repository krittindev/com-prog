def text2keys(text):

    text_key = {' ': '0'}
    for i in range(15):
        key = i // 3 + 2
        multiplier = i % 3 + 1
        text_key[chr(ord('a') + i)] = str(key) * multiplier
    for i in range(4):
        key = 7
        multiplier = i + 1
        text_key[chr(ord('p') + i)] = str(key) * multiplier
    for i in range(3):
        key = 8
        multiplier = i + 1
        text_key[chr(ord('t') + i)] = str(key) * multiplier
    for i in range(4):
        key = 9
        multiplier = i + 1
        text_key[chr(ord('w') + i)] = str(key) * multiplier

    keys = ''
    list_key = []
    lower_text = text.lower()
    for c in lower_text:
        if c.isalpha() or c == ' ':
            list_key.append(text_key[c])
    keys = ' '.join(list_key)
    return keys


def keys2text(keys):

    key_text = {'0': ' '}
    for i in range(15):
        key = i // 3 + 2
        multiplier = i % 3 + 1
        key_text[str(key) * multiplier] = chr(ord('a') + i)
    for i in range(4):
        key = 7
        multiplier = i + 1
        key_text[str(key) * multiplier] = chr(ord('p') + i)
    for i in range(3):
        key = 8
        multiplier = i + 1
        key_text[str(key) * multiplier] = chr(ord('t') + i)
    for i in range(4):
        key = 9
        multiplier = i + 1
        key_text[str(key) * multiplier] = chr(ord('w') + i)

    text = ''
    list_key = keys.split()
    for key in list_key:
        text += key_text[key]

    return text


# ตอ้ งมคี ําสั่งขํา้ งล่ํางน้ี ตอนสง่ ให้Grader ตรวจ
exec(input().strip())
