class Complex:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        if self.a == 0 and self.b == 0:
            return "0"

        str_a = ""
        str_b = ""

        if self.a == 0:
            pass
        elif isinstance(self.a, int):
            str_a = "%d" % self.a
        elif isinstance(self.a, float):
            str_a = "%.1f" % self.a
        if self.b == 0:
            pass
        elif self.b == 1:
            str_b = "i"
        elif self.b == -1:
            str_b = "-i"
        elif isinstance(self.b, int):
            str_b = "%di" % self.b
        elif isinstance(self.b, float):
            str_b = "%.1fi" % self.b

        if self.a != 0 and self.b > 0:
            return str_a + "+" + str_b
        else:
            return str_a + str_b

    def __add__(self, rhs):
        a = self.a + rhs.a
        b = self.b + rhs.b
        return Complex(a, b)

    def __mul__(self, rhs):
        a = self.a
        b = self.b
        c = rhs.a
        d = rhs.b
        return Complex(a * c - b * d, a * d + b * c)

    def __truediv__(self, rhs):
        a = self.a
        b = self.b
        c = rhs.a
        d = rhs.b
        _a = (a * c + b * d) / (c ** 2 + d ** 2)
        _b = (-a * d + b * c) / (c ** 2 + d ** 2)
        return Complex(_a, _b)


t, a, b, c, d = [int(x) for x in input().split()]
c1 = Complex(a, b)
c2 = Complex(c, d)
if t == 1:
    print(c1)
elif t == 2:
    print(c2)
elif t == 3:
    print(c1+c2)
elif t == 4:
    print(c1*c2)
else:
    print(c1/c2)
