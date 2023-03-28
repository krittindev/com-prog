def abbrev_num(n):
    K = 10**3
    M = 10**6
    B = 10**9
    if n < K:
        return n
    elif n < K*10:
        return "{:.1f}K".format(n / K)
    elif n < M:
        return "{:.0f}K".format(n / K)
    elif n < M*10:
        return "{:.1f}M".format(n / M)
    elif n < B:
        return "{:.0f}M".format(n / M)
    elif n < B*10:
        return "{:.1f}B".format(n / B)
    else:
        return "{:.0f}B".format(n / B)
print(abbrev_num(int(input())))
# print(abbrev_num(32))
# print(abbrev_num(8456))
# print(abbrev_num(84560))
# print(abbrev_num(108283))
# print(abbrev_num(2293910))
# print(abbrev_num(12999995))
# print(abbrev_num(580912391))
# print(abbrev_num(1301008191))
# print(abbrev_num(25555555555))
# print(abbrev_num(2555555555555))