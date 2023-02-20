x = [int(e) for e in input().split()]
k = int(input())

x.append(0)

previous_n = None
total = 0

sub_l = []

for n in x:
    if previous_n != n:
        if len(sub_l) < k:
            total += sum(sub_l)
        sub_l = [n]
    else:
        sub_l.append(n)
    previous_n = n

print(total)
