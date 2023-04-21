n = int(input().strip())

genres_sum_time = {}

for _ in range(n):
    *__, genre, str_time = [e.strip() for e in input().strip().split(',')]
    minute, second = [int(e) for e in str_time.split(':')]
    time = minute * 60 + second

    if genre not in genres_sum_time:
        genres_sum_time[genre] = 0

    genres_sum_time[genre] += time

genre_by_time = [
    (genre, -time)
    for time, genre in sorted([
        (-time, genre)
        for genre, time in genres_sum_time.items()
    ])
][:3]

for genre, time in genre_by_time:
    minute = time // 60
    second = time % 60
    print('%s --> %d:%02d' % (genre, minute, second))
