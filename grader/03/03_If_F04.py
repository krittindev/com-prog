
def is_mobile_number(number):
    return True if len(number) == 10 and number[0:2] in ["06", "08", "09"] else False
exec(input()) # DON'T remove this line