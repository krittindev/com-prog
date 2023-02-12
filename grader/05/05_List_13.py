isAppend = True
n = int(input())
l = []

for _ in range(n):
    if isAppend:
        l.append(int(input()))
    else:
        l.insert(0, int(input()))
    isAppend = not isAppend

for n in [int(e) for e in input().split()]:
    if isAppend:
        l.append(n)
    else:
        l.insert(0, n)
    isAppend = not isAppend

while True:
    n = int(input())
    if n == -1:
        break
    if isAppend:
        l.append(n)
    else:
        l.insert(0, n)
    isAppend = not isAppend

print(l)