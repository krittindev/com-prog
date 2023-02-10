def to_frame(s):
    frame = []
    sub_frame = []
    n_frame = 1
    times_of_frame = 0

    for c in s:
        times_of_frame += 1

        if n_frame == 10:
            if times_of_frame == 1:
                if c == 'X':
                    score = 10
                    sub_frame.append(score)
                else:
                    score = int(c)
                    sub_frame.append(score)
            if times_of_frame == 2:
                if c == 'X':
                    score = 10
                    sub_frame.append(score)
                else:
                    if c == '/':
                        score = 10 - sub_frame[times_of_frame - 2]
                        sub_frame.append(score)
                    else:
                        score = int(c)
                        sub_frame.append(score)
                        frame.append(sub_frame)
            if times_of_frame == 3:
                if c == 'X':
                    score = 10
                    sub_frame.append(score)
                else:
                    if c == '/':
                        score = 10 - sub_frame[times_of_frame - 2]
                        sub_frame.append(score)
                    else:
                        score = int(c)
                        sub_frame.append(score)
                frame.append(sub_frame)
        else:
            if c == 'X':
                score = 10
                frame.append([score])
                times_of_frame = 0
                n_frame += 1
            else:
                if c == '/':
                    score = 10 - sub_frame[0]
                    sub_frame.append(score)
                else:
                    score = int(c)
                    sub_frame.append(score)

                if times_of_frame == 2:
                    frame.append(sub_frame)
                    times_of_frame = 0
                    sub_frame = []
                    n_frame += 1
    return frame

def sum_next_n_frames(frame, n_frame, n):
    return sum([score for sub_frame in frame[n_frame:] for score in sub_frame][:n])

def get_scores(frame):
    scores = []
    for n_frame in range(1, 10 + 1):
        i = n_frame - 1
        sub_frame = frame[i]
        if (n_frame == 10):
            scores.append(sum(sub_frame))
        else:
            if sum(sub_frame) == 10:
                if len(sub_frame) == 1: # X case
                    scores.append(sum(sub_frame) + sum_next_n_frames(frame, n_frame, 2))
                elif len(sub_frame) == 2: # / case
                    scores.append(sum(sub_frame) + sum_next_n_frames(frame, n_frame, 1))
            else: 
                scores.append(sum(sub_frame))
    return scores

s = input()
target_frame = int(input())

frame = to_frame(s)
scores = get_scores(frame)

if target_frame in range(1, 10 + 1):
    i = target_frame - 1
    print(scores[i])
else:
    print(sum(scores))