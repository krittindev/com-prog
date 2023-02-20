import math
    
def maximize(d, f, r):
    d, f, r = int(d), int(f + r) - int(f if f != '' else 0), int('9' * len(r) + '0' * len(f))
    # print(d, f, r)
    return d, f, r
    
def dec2frac(d, f, r):
    numerator, denominator = d * r + f, r
    # print(numerator, denominator)
    return numerator, denominator

def minimize(a, b):
    a, b = a // math.gcd(a, b), b // math.gcd(a, b)
    # print(a, b)
    return a, b

d, f, r = [e for e in input().split(',')]
d, f, r = maximize(d, f, r)
numerator, denominator = dec2frac(d, f, r)
numerator, denominator = minimize(numerator, denominator)
print(numerator, '/', denominator)