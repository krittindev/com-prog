def main():
    n = int(input().strip())

    if n < 1:
        print('0\n0')
        return

    list_set = []

    for _ in range(n):
        each_set = set(int(e) for e in input().strip().split())
        list_set.append(each_set)

    print(len(set.union(*list_set)))
    print(len(set.intersection(*list_set)))


main()
