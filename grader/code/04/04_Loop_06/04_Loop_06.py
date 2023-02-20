def print_triangle(h):
    print('.' * (h - 1) + '*')
    for i in range(h - 2):
        print('.' * (h - i - 2) + '*' + '.' * (i * 2 + 1) + '*')
    print('*' * (h * 2 - 1))

def test():
    print_triangle(2)
    print_triangle(3)
    print_triangle(4)

# test()
h = int(input())
print_triangle(h)