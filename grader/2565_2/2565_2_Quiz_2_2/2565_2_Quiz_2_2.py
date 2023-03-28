def match(s, cs):
    index_s = 0
    index_cs = 0
    container = []
    is_in_bracket = False

    while index_s < len(s) and index_cs < len(cs):
        # print(index_s, index_cs, container, is_in_bracket)
        if is_in_bracket:
            if cs[index_cs] not in '])':
                container.append(cs[index_cs])
            else:
                if cs[index_cs] == ']':
                    if s[index_s] not in container:
                        return False
                elif cs[index_cs] == ')':
                    if s[index_s] in container:
                        return False
                is_in_bracket = False
                container = []
                index_s += 1
        elif cs[index_cs] in '[(':
            is_in_bracket = True
        elif cs[index_cs] == '?':
            index_s += 1
        else:
            if s[index_s] != cs[index_cs]:
                return False
            else:
                index_s += 1
        index_cs += 1

    if index_s < len(s) or index_cs < len(cs):
        return False
    return True


# ห้ามลบหรือแก้ไขบรรทัดด้านล่างนี5
exec(input())
