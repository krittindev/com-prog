class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y
n = int(input())
points = []
for _ in range(n):
    x, y = [int(e) for e in input().split()]
    points.append(Point(x, y))
order = input()
if order == "Zig-Zag":
    zmin = min(points[i].x if i % 2 == 0 else points[i].y for i in range(len(points)))
    zmax = max(points[i].x if i % 2 != 0 else points[i].y for i in range(len(points)))
    print(zmin, zmax)
elif order == "Zag-Zig":
    zmin = min(points[i].x if i % 2 != 0 else points[i].y for i in range(len(points)))
    zmax = max(points[i].x if i % 2 == 0 else points[i].y for i in range(len(points)))
    print(zmin, zmax)
