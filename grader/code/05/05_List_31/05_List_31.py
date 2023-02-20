l = input().split()
orders = input()
for order in orders:
    if order == 'C':
        l = l[len(l) // 2:] + l[:len(l) // 2]
    elif order == 'S':
        l = [l[i // 2] if i % 2 == 0 else l[len(l) // 2 + (i - 1) // 2] for i in range(len(l))]
print(' '.join(l))