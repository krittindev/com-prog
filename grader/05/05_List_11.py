def missing_digits(t):
    missing_digits_list = [str(e) for e in range(10) if not str(e) in t]
    return missing_digits_list

t = input().strip()
missing_digits_list = missing_digits(t)
if len(missing_digits_list) == 0:
    print("None")
else:
    print(','.join(missing_digits_list))