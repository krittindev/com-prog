def make_int_list(x):
    return [int(e) for e in x.split()]


def is_odd(e):
    return e % 2 != 0


def odd_list(alist):
    return [e for e in alist if is_odd(e)]


def sum_square(alist):
    return sum(e * e for e in alist)


exec(input().strip())
