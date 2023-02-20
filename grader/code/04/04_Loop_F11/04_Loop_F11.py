def RLE(t):
    l = []
    temp_c = ''
    sum = 0
    for e in t:
        if e == temp_c:
            sum += 1
        if e != temp_c:
            if sum != 0:
                l.append([temp_c, sum])
            temp_c = e
            sum = 1
    if sum != 0:
        l.append([temp_c, sum])
    return l
    
exec(input()) # DON'T remove this line