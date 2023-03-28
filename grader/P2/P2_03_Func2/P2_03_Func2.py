def convex_polygon_area(p):
    len_p = len(p)
    det = max(
        abs(sum(
            p[i % len_p][0] * p[(i + 1) % len_p][1]
            - p[i % len_p][1] * p[(i + 1) % len_p][0]
            for i in range(len_p + 1)
        )),
        abs(sum(
            p[i % len_p][0] * p[(i + 1) % len_p][1]
            - p[i % len_p][1] * p[(i + 1) % len_p][0]
            for i in range(-len_p, 0)
        ))
    )
    _convex_polygon_area = 1 / 2 * det
    return _convex_polygon_area


def is_heterogram(s):
    sorted_lower_s = sorted([c for c in s.lower() if c.isalpha()])
    _is_heterogram = all(sorted_lower_s[i] != sorted_lower_s[i + 1]
                         for i in range(len(sorted_lower_s) - 1))
    return _is_heterogram


def replace_ignorecase(s, a, b):
    _replace_ignorecase = ''
    len_sub = 1
    len_s = len(s)
    len_a = len(a)
    lower_s = s.lower()
    lower_a = a.lower()
    for i in range(len(s)):
        if lower_s[i + 1 - len_sub: i + 1] == lower_a[: len_sub]:
            if len_sub == len_a:
                _replace_ignorecase += b
                len_sub = 1
            elif i == len_s - 1:
                _replace_ignorecase += s[i + 1 - len_sub: i + 1]
            else:
                len_sub += 1
        else:
            _replace_ignorecase += s[i + 1 - len_sub: i + 1]
            len_sub = 1
    return _replace_ignorecase


def top3(votes):
    _top3 = [id for id, _ in [[id, -score]
             for score, id in sorted([-score, id] for id, score in votes.items())]][:3]
    return _top3


for k in range(2):
    exec(input().strip())
