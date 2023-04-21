def knows(R, x, y):
    return y in R[x]


def is_celeb(R, x):
    if any(y != x for y in R[x]):
        return False
    if any(_x != x and not knows(R, _x, x) for _x in R.keys()):
        return False
    return True


def find_celeb(R):
    for x in R.keys():
        if is_celeb(R, x):
            return x

    return None


def read_relations():
    R = dict()

    while True:
        d = input().split()

        if len(d) == 1:
            break
        x, y = d

        if x not in R:
            R[x] = set()

        if y not in R:
            R[y] = set()

        R[x].add(y)

    return R


def main():
    R = read_relations()
    c = find_celeb(R)

    if c == None:
        print('Not Found')
    else:
        print(c)


exec(input().strip())  # do not remove this line
