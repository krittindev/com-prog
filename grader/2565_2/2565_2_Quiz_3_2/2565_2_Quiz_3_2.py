def print_seats(assignments, n_rows, n_cols):
    seat_people = {}

    for seat in range(n_rows * n_cols):
        seat_people[seat + 1] = "--"

    for name, seat in assignments:
        seat_people[seat] = name
    for row in range(n_rows):
        print("|", end="")
        for col in range(n_cols):
            print(" %s |" % seat_people[row * n_cols + col + 1], end="")
        print()


exec(input().strip())  # DO NOT remove this line
