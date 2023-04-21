n = int(input().strip())
id_cities = {}
city_ids = {}
ids = []
for _ in range(n):
    line = input().strip()
    id, cities = line.split(': ')
    cities = cities.split(', ')
    for city in cities:
        if city not in city_ids:
            city_ids[city] = set()
        city_ids[city].add(id)
    id_cities[id] = set(cities)
    ids.append(id)

target_id = input()
ids_set = set.union(*[city_ids[city]
                    for city in id_cities[target_id]]) - {target_id}
if len(ids_set) != 0:
    result = []
    for id in ids:
        if id in ids_set:
            result.append(id)
    print('\n'.join(result))
else:
    print('Not Found')
