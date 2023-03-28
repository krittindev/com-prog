def get_ranks():
    ranks_text = 'A23456789TJQK'
    ranks_dict = {}
    for i in range(len(ranks_text)):
        ranks_dict[ranks_text[i]] = i + 1
    return ranks_dict


def get_suits():
    suits_text = 'CDHS'
    suits_dict = {}
    for i in range(len(suits_text)):
        suits_dict[suits_text[i]] = i + 1
    return suits_dict


def get_diff(first, second):
    ranks = get_ranks()
    suits = get_suits()

    first_ranks = ranks[first[0]]
    first_suits = suits[first[1]]
    second_ranks = ranks[second[0]]
    second_suits = suits[second[1]]

    if first_ranks == second_ranks:
        if first_suits == second_suits:
            return '0'
        elif first_suits < second_suits:
            return '-{}'.format(second_suits - first_suits)
        elif first_suits > second_suits:
            return '+{}'.format(first_suits - second_suits)
    elif first_ranks < second_ranks:
        return '-{}'.format(second_ranks - first_ranks)
    elif first_ranks > second_ranks:
        return '+{}'.format(first_ranks - second_ranks)


def main():

    text = input().strip()
    result = ''

    for i in range(len(text) // 2 - 1):
        first = text[i * 2: i * 2 + 2]
        second = text[i * 2 + 2: i * 2 + 4]
        result += get_diff(first, second)

    print(result)


main()
