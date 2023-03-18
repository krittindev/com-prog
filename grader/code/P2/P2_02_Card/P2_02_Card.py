values = 'A23456789TJQK'
sets = 'CDSH'

seq = input().strip()

pairs = []

for i in range(len(seq) // 2 - 1):
    pairs.append([seq[i: i+2], seq[i+2:i+4]])

for a, b in pairs:
    if a
