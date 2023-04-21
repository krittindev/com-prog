def add_poly(p1, p2):
    dict_degree_coefficient = {}
    negative_degree_coefficient = []
    coefficient_degree = []

    for coefficient, degree in [*p1, *p2]:
        if degree in dict_degree_coefficient:
            dict_degree_coefficient[degree] += coefficient
        else:
            dict_degree_coefficient[degree] = coefficient

    for degree, coefficient in dict_degree_coefficient.items():
        if coefficient != 0:
            negative_degree_coefficient.append((-degree, coefficient))

    for degree, coefficient in sorted(negative_degree_coefficient):
        coefficient_degree.append((coefficient, -degree))

    return coefficient_degree


def recursively_add(terms):
    if len(terms) < 2:
        return terms

    if len(terms) == 2:
        return add_poly([terms[0]], [terms[1]])

    return add_poly([terms[0]], recursively_add(terms[1:]))


def mult_poly(p1, p2):
    all_term = []

    for c1, d1 in p1:
        for c2, d2 in p2:
            coefficient = c1 * c2
            degree = d1 + d2
            all_term.append((coefficient, degree))

    terms = recursively_add(all_term)

    return terms


# ต้องมีสองค ําสั่งข้ํางล่ํางนี้ ตอนส่งให้ Grader ตรวจ
for i in range(3):
    exec(input().strip())
