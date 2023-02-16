x = [int(e) for e in input().split()]
k = int(input())

x.append(0)

curr_e = None
count = 0
total = 0

l = []
sub_l = []

for e in x:
    if curr_e !=  e:
        if len(sub_l) < k:
            l.append(sub_l)
            total += sum(sub_l)
        sub_l = [e]
    else:
        sub_l.append(e)
    curr_e = e
        
print(total)        
