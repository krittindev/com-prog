import math

def first_root(a, b, c):
    numerator = -b - math.sqrt(b ** 2 - 4 * a * c)
    denominator = 2 * a
    return round(numerator / denominator, 3)
def second_root(a, b, c):
    numerator = -b + math.sqrt(b ** 2 - 4 * a * c)
    denominator = 2 * a
    return round(numerator / denominator, 3)

a = float(input())
b = float(input())
c = float(input())

print(first_root(a, b, c), second_root(a, b, c))