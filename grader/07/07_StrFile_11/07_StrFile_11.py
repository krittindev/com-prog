text = input().strip()
if text[-1] == 's' or text[-1] == 'x' or text[-2:] == 'ch':
    print(text + 'es')
elif text[-1] == 'y':
    if text[-2] not in 'aeiou':
        print(text[:len(text) - 1] + 'ies')
    else:
        print(text + 's')
else:
    print(text + 's')
