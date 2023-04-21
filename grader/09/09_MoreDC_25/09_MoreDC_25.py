def row_number(t, e):  # return row number of t containing e (top row is row #0)
    for i in range(len(t)):
        if e in t[i]:
            return i
    return -1


def flatten(t):
    flatten_t = []
    _ = [[flatten_t.append(e) for e in row if e != 0] for row in t]
    return flatten_t


def inversions(x):
    _inversions = 0
    len_x = len(x)
    for i in range(len_x):
        for j in range(i, len_x):
            a = x[i]
            b = x[j]
            if a > b:
                _inversions += 1
    return _inversions


def solvable(t):
    amount_row = len(t)
    amount_inversions = inversions(flatten(t))
    row_number_0 = row_number(t, 0)
    if amount_row % 2 != 0 and amount_inversions % 2 == 0:
        return True
    if amount_row % 2 == 0:
        if amount_inversions % 2 != 0 and row_number_0 % 2 == 0:
            return True
        if amount_inversions % 2 == 0 and row_number_0 % 2 != 0:
            return True
    return False


exec(input().strip())  # do not remove this line
