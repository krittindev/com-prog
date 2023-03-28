def complex_replace(s, k_strs, r_strs):
    new_s = ''
    indices_find = [s.find(e) for e in k_strs]
    for i in range(len(indices_find)):
        if indices_find[i] == -1:
            indices_find[i] = 10e10
    if len(indices_find) == 0:
        return s
    min_indices_find = min(indices_find)
    index_min_indies_find = indices_find.index(min_indices_find)
    index = 0
    while index < len(s):
        if index == min_indices_find:
            new_s += '<' + r_strs[index_min_indies_find] + '>'
            index += len(k_strs[index_min_indies_find])
        else:
            new_s += s[index]
            index += 1

    return new_s


# ห้ามลบหรือแก้ไขบรรทัดด้านล่างนี<
exec(input())
