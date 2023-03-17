# mini heart
# submit https://www.mycourseville.com/?q=courseville/worksheet/32196/901789
# [your ID].py

def show_mini_haert(n):
    for i in range(n // 2):
        print('.' * (n // 2 - i - 1) + '#' * (n - (n // 2 - i - 1) * 2) + '.' * (n // 2 - i - 1) +
              '.' + '.' * (n // 2 - i - 1) + '#' * (n - (n // 2 - i - 1) * 2) + '.' * (n // 2 - i - 1))
    for i in range(n//2-2):
        print("#" * int(2 * n + 1))
    for i in range(n + 1):
        print('.' * (i) + '#' * (n - i) + '#' + '#' * (n - i) + '.' * (i))


def test():
    show_mini_haert(4)
    print()
    show_mini_haert(5)
    print()
    show_mini_haert(6)
    print()
    show_mini_haert(9)
# test()


n = int(input())
