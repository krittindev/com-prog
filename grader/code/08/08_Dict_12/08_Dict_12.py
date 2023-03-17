n = int(input().strip())
first2last = {}
last2first = {}
for _ in range(n):
  first, last = input().strip().split()
  first2last[first] = last
  last2first[last] = first
m = int(input().strip())
for _ in range(m):
  name = input().strip()
  if name not in first2last and name not in last2first:
    print('Not found')
  elif name in first2last:
    print(first2last[name]) 
  else:
    print(last2first[name])