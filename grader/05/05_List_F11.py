def missing_digits(t):
    missing_digits_list = [e for e in range(10) if not str(e) in t]
    return missing_digits_list
exec(input()) # DON'T remove this line