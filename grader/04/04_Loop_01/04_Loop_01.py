l = []
while True:
    n = input()
    if n != 'q':
        l.append(float(n))
    else:
        break
if len(l) == 0:
    print("No Data")
else:
    print(round(sum(l) / len(l), 2))