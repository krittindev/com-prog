import math

def lower_bound(n):
  a = math.sqrt(2 * math.pi) 
  b = n ** (n + 1 / 2)
  c = math.e ** (-n + 1 / (12 * n + 1))
  return a * b * c
  
def upper_bound(n):
  a = math.sqrt(2 * math.pi) 
  b = n ** (n + 1 / 2)
  c = math.e ** (-n + 1 / (12 * n))
  return a * b * c

n = float(input())
print(lower_bound(n))
print(upper_bound(n))