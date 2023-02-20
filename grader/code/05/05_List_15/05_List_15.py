all_n = [int(e) for e in input().split()]
all_n = sorted(all_n)
unique = []
unique_n = 0
for i in range(len(all_n) - 1):
    if all_n[i] != all_n[i + 1]:
        if unique_n == 0:
            unique.append(all_n[i])
        unique_n += 1
        if unique_n < 10:
            unique.append(all_n[i + 1])
unique_n += 1
print(unique_n)
print(unique)