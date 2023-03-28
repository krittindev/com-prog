num = int(input())

if num < 0:
    print("negative")
elif num == 0:
    print("zero")
else:
    print("positive")

if num % 2 != 0:
    print("odd")
else:
    print("even")