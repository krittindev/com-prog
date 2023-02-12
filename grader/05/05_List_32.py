q = list()
first_tickect = -1
curr_ticket = -1
curr_call = -1
n = int(input())
for k in range(n):
    c = input().split()
    if c[0] == 'reset':
        first_tickect = int(c[1])
    elif c[0] == 'new':
        time = int(c[1])
        if curr_ticket == -1:
            curr_ticket = first_tickect - 1
        curr_ticket += 1
        print('ticket', curr_ticket)
        q.append([curr_ticket, time])
    elif c[0] == 'next':
        if curr_call == -1:
            curr_call = first_tickect - 1
        curr_call += 1
        print( 'call', curr_call)
    elif c[0] == 'order':
        time = int(c[1])
        i = [i for i in range(len(q)) if q[i][0] == curr_call][0]
        q[i] = [q[i][0], q[i][1], time - q[i][1]]
        print( 'qtime', curr_call, q[i][2])
    elif c[0] == 'avg_qtime':
        ordered_q = [e[2] for e in q if len(e) == 3]
        print( 'avg_qtime', round(sum(ordered_q) / len(ordered_q),4) )