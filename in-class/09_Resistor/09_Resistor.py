first_bands = {'black': None, 'brown': 1, 'red': 2, 'orange': 3, 'yellow': 4, 'green': 5,
               'blue': 6, 'violet': 7, 'grey': 8, 'white': 9, 'gold': None, 'silver': None}
second_bands = {'black': 0, 'brown': 1, 'red': 2, 'orange': 3, 'yellow': 4, 'green': 5,
                'blue': 6, 'violet': 7, 'grey': 8, 'white': 9, 'gold': None, 'silver': None}
third_bands = {'black': 0, 'brown': 1, 'red': 2, 'orange': 3, 'yellow': 4, 'green': 5,
               'blue': 6, 'violet': 7, 'grey': 8, 'white': 9, 'gold': None, 'silver': None}
multipliers = {'black': 1e0, 'brown': 1e1, 'red': 1e2, 'orange': 1e3, 'yellow': 1e4, 'green': 1e5,
               'blue': 1e6, 'violet': 1e7, 'grey': 1e8, 'white': 1e9, 'gold': 1e-1, 'silver': 1e-2}
torelances = {'black': None, 'brown': 1, 'red': 2, 'orange': None, 'yellow': None, 'green': 0.5,
              'blue': 0.25, 'violet': 0.10, 'grey': 0.05, 'white': None, 'gold': 5, 'silver': 10}


def get_resistor(colors):
    for color in colors:
        if color not in first_bands:
            return 'Program Error'
    if len(colors) == 4:
        first_band = first_bands[colors[0]]
        second_band = second_bands[colors[1]]
        multiplier = multipliers[colors[2]]
        torelance = torelances[colors[3]]
        if first_band == None or second_band == None or multiplier == None or torelance == None:
            return 'Program Error'
        resistor = ((first_band * 10 + second_band * 1) * multiplier)
        return 'Resistor: %g Ohms\nError: %g%%' % (resistor, torelance)
    elif len(colors) == 5:
        first_band = first_bands[colors[0]]
        second_band = second_bands[colors[1]]
        third_band = third_bands[colors[2]]
        multiplier = multipliers[colors[3]]
        torelance = torelances[colors[4]]
        if first_band == None or second_band == None or third_band == None or multiplier == None or torelance == None:
            return 'Program Error'
        resistor = ((first_band * 100 +
                    second_band * 10 + third_band * 1) * multiplier)
        return 'Resistor: %g Ohms\nError: %g%%' % (resistor, torelance)
    else:
        return 'Program Error'


def main():
    colors = input().strip().split(',')
    print(get_resistor(colors))


main()
