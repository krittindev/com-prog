# [09_MoreDC_23] 10_TSD_★★_GenreTotalPlaytime
s = {}
t = []
for i in range(int(input())):
    song, singer, stlye, time = input().strip().split(', ')

    time = (int(time[:-3])*60) + int(time[-2:])

    if stlye not in s:
        s[stlye] = time
    else:
        s[stlye] = int(s[stlye])+int(time)

x = [(k, v) for k, v in sorted(s.items(), key=lambda item: item[1])]


for stlye, time1 in x:

    if len(str(time1 % 60)) == 1:
        t.append(stlye + ' --> ' + str(time1//60) +
                 ':' + '0' + str(time1 % 60))
    else:
        t.append(stlye + ' --> ' + str(time1//60) + ':' + str(time1 % 60))
if len(t) >= 3:
    print(t[-1])
    print(t[-2])
    print(t[-3])
elif len(t) == 2:
    print(t[-1])
    print(t[-2])
