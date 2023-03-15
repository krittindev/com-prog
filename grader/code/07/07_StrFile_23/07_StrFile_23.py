def fileMinMaxAverage(data, year):

    filteredScores = []
    for line in data:
        id, score = line.strip().split()
        score = float(score)
        isSameYear = year[-2:] == id[:2]
        if isSameYear:
            filteredScores.append(score)

    if len(filteredScores) == 0:
        return 'No data'

    return '{} {} {}'.format(
        min(filteredScores),
        max(filteredScores),
        sum(filteredScores) / len(filteredScores)
    )


fileName, year = input().strip().split()
data = open(fileName, 'r')

print(fileMinMaxAverage(data, year))
