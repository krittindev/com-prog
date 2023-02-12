l = []
n = int(input())
l.append(n)
while n != 1:
    if n % 2 == 0:
        n = n // 2
    else:
        n = 3 * n + 1
    l.append(n)
print('->'.join(str(e) for e in (l if len(l) < 15 else l[-15:])))