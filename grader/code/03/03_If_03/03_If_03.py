def find_max(l):
    max_n = l[0]
    for e in l[1:]:
        if max_n < e:
            max_n = e
    return max_n

def find_min(l):
    min_n = l[0]
    for e in l[1:]:
        if min_n > e:
            min_n = e
    return min_n

l = [float(e) for e in input().split()]
print(round((sum(l) - find_max(l) - find_min(l)) / 2.0, 2))