stations = {}
current_station = ""

while True:
    input_str = input().strip()
    if len(input_str.split()) == 2:
        first, second = input_str.split()
        if first in stations:
            stations[first].append(second)
        else:
            stations[first] = [second]
        if second in stations:
            stations[second].append(first)
        else:
            stations[second] = [first]
    else:
        current_station = input_str
        if current_station not in stations:
            stations[current_station] = []
        break

destinations = set()

for first in stations[current_station]:
    destinations.add(first)
    for second in stations[first]:
        destinations.add(second)

destinations = destinations | {current_station}

for station in sorted(list(destinations)):
    print(station)
