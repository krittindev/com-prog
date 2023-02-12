def distance(x, y):
    return (x**2 + y**2)**0.5
n = int(input())
l = []
for order in range(1, n + 1):
    x, y = [float(e) for e in input().split()]
    l.append([distance(x, y), order, x, y])

l.sort()
print('#{}: ({:.2f}, {:.2f})'.format(l[2][1], l[2][2], l[2][3]))