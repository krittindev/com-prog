import math

def mosteller(w, h):
  return math.sqrt(w * h) / 60
def haycock(w, h):
  return 0.024265 * w ** 0.5378 * h ** 0.3964
def boyd(w, h):
  return 0.0333 * w ** (0.6157 - 0.0188 * math.log(w, 10)) * h ** 0.3

w = float(input())
h = float(input())

print(mosteller(w, h))
print(haycock(w, h))
print(boyd(w, h))