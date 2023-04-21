n = int(input().strip())

winners = set()
losers = set()

for _ in range(n):
    winner, loser = input().strip().split()
    winners.add(winner)
    losers.add(loser)

winner = list(winners - losers)

print(sorted(winner))
