def no_lowercase(t):  # return True if no lowercase, otherwise return False
    alphabets = 'qwertyuiopasdfghjklzxcvbnm'
    for c in t:
        if c in alphabets:
            return False
    return True


def no_uppercase(t):
    alphabets = 'qwertyuiopasdfghjklzxcvbnm'.upper()
    for c in t:
        if c in alphabets:
            return False
    return True


def no_number(t):
    numbers = '0123456789'
    for c in t:
        if c in numbers:
            return False
    return True


def no_symbol(t):
    symbols = '!@#$%^&*()_+~`-={[}]|\\:;"\'<,>.?/'
    for c in t:
        if c in symbols:
            return False
    return True


def character_repetition(t):
    for c in t:
        if c * 4 in t:
            return True
    return False


def number_sequence(t):
    numbers = '01234567890'
    for i in range(len(t) - 3):
        if t[i: i + 4] in numbers or \
                t[i: i + 4] in numbers[::-1]:
            return True
    return False


def letter_sequence(t):
    alphabets = 'abcdefghijklmnopqrstuvwxyz'
    for i in range(len(t) - 3):
        if t[i: i + 4].lower() in alphabets or \
                t[i: i + 4].lower() in alphabets[::-1]:
            return True
    return False


def keyboard_pattern(t):
    keyboard = '!@#$%^&*()_+~`-={[}]|\\:;"\'<,>.?/'
    keyboard += 'qwertyuiopasdfghjklzxcvbnm'
    for i in range(len(t) - 3):
        if t[i: i + 4].lower() in keyboard or \
                t[i: i + 4].lower() in keyboard[::-1]:
            return True
    return False


# -----------------------------
passw = input().strip()
errors = []
if len(passw) < 8:
    errors.append("Less than 8 characters")

if no_lowercase(passw):
    errors.append("No lowercase letters")

if no_uppercase(passw):
    errors.append("No uppercase letters")

if no_number(passw):
    errors.append("No numbers")

if no_symbol(passw):
    errors.append("No symbols")

if character_repetition(passw):
    errors.append("Character repetition")

if number_sequence(passw):
    errors.append("Number sequence")

if letter_sequence(passw):
    errors.append("Letter sequence")

if keyboard_pattern(passw):
    errors.append("Keyboard pattern")

if len(errors) == 0:
    print("OK")
else:
    print('\n'.join(errors))
