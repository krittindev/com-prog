text = input().strip()
alphas = {}
for char in text:
  if not ('a' <= char.lower() <= 'z'): continue
  if char.lower() not in alphas:
    alphas[char.lower()] = -1
  else:
    alphas[char.lower()] -= 1
    
l = sorted([[count, alpha]for alpha, count in alphas.items()])

for count, alpha in l:
  print(alpha, '->', -count)