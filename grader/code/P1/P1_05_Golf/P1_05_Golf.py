import math

pars = []
strokes = []
chooses = []
maintain_strokes = []

for _ in range(9):
    par, stroke, choose = [int(e) for e in input().split()]
    pars.append(par)
    strokes.append(stroke)
    chooses.append(choose)
    if choose == 1:
        maintain_strokes.append(min(par + 2, stroke))
    

handicap = math.floor(0.8 * (1.5 * sum(maintain_strokes) - sum(pars)))
total_score = sum(strokes) - handicap

print(sum(strokes), handicap, total_score, sep = '\n')