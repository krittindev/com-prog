def distance1(x1, y1, x2, y2):
    return ((x1 - x2)**2 + (y1 - y2)**2)**0.5


def distance2(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return distance1(x1, y1, x2, y2)


def distance3(c1, c2):
    x1, y1, r1 = c1
    x2, y2, r2 = c2
    d = distance1(x1, y1, x2, y2)
    return d, d - r1 - r2 <= 0


def perimeter(points):
    total = 0
    for i in range(-1, len(points) - 1):
        x1, y1 = points[i]
        x2, y2 = points[i + 1]
        total += distance1(x1, y1, x2, y2)
    return total


exec(input().strip())
