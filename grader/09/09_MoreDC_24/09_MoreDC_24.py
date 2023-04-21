species = []
species_names = {}

while True:
    line = input().strip()

    if line == 'q':
        break

    name, specie = (e.strip() for e in line.strip().split(','))

    if specie not in species:
        species.append(specie)
        species_names[specie] = []

    species_names[specie].append(name)

for specie in species:
    names = species_names[specie]
    print('%s: %s' % (specie, ', '.join(names)))
