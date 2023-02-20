number = input()
print("Mobile number" if len(number) == 10 and number[0:2] in ["06", "08", "09"] else "Not a mobile number")