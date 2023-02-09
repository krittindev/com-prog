zig_zag_min = 100
zig_zag_max = -100
zag_zig_min = 100
zag_zig_max = -100
is_zig = True
while True:
    s = input()
    if ' ' in s: # input is pair of number
        x, y = s.split()
        if is_zig:
            zig_zag_min = min(zig_zag_min, int(x))
            zig_zag_max = max(zig_zag_max, int(y))
            zag_zig_min = min(zag_zig_min, int(y))
            zag_zig_max = max(zag_zig_max, int(x))
            # print(is_zig, zig_zag_min, zig_zag_max, zag_zig_min, zag_zig_max)
        else:
            zag_zig_min = min(zag_zig_min, int(x))
            zag_zig_max = max(zag_zig_max, int(y))
            zig_zag_min = min(zig_zag_min, int(y))
            zig_zag_max = max(zig_zag_max, int(x))
            # print(is_zig, zig_zag_min, zig_zag_max, zag_zig_min, zag_zig_max)
    if s == "Zig-Zag":
        print(zig_zag_min, zig_zag_max)
        break
    elif s == "Zag-Zig":
        print(zag_zig_min, zag_zig_max)
        break
    is_zig = not is_zig