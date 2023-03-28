budget = int(input().strip())
bookings = []
lots = []

while True:
    line = input().strip()
    if line == 'Q':
        break
    else:
        splited_line = line.split()
        id, amount = splited_line[0], int(splited_line[1])
        bookings.append([id, amount])
        lots.append([id, 0])


k = 0

while budget > 0:
    if lots[k][1] < bookings[k][1]:
        budget -= 1
        lots[k][1] += 1
    k = (k + 1) % len(bookings)

for id, amount in lots:
    print(id, amount)
