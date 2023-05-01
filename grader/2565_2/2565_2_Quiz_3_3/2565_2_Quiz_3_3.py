sport_players = {}
department_student_infos = {}
sport_departments = {}

while True:
    line = input().strip()
    
    if line == "END":
        break
    
    sport, _players = line.split()
    players = int(_players)
    sport_players[sport] = players
    sport_departments[sport] = {}
    
while True:
    line = input().strip()
    
    if line == "END":
        break
    
    student, department, _sports = line.split()
    sports = _sports.split(',')
    
    if department not in department_student_infos:
        department_student_infos[department] = {}
    
    if student not in department_student_infos[department]:
        department_student_infos[department][student] = set(sports)
    else:
        _sports = department_student_infos[department][student]
        department_student_infos[department][student] = set(sports) | _sports
    
for department, students in department_student_infos.items():
    for student, sports in students.items():
        for sport in sports:
            if department not in sport_departments[sport]:
                sport_departments[sport][department] = 1
            else:
                sport_departments[sport][department] += 1

for sport in sorted(sport_departments.keys()):
    print(sport, end = ":")
    for department in sorted(sport_departments[sport].keys()):
        players = sport_departments[sport][department]
        if players >= sport_players[sport]:
            teams = players // sport_players[sport]
            spares = players % sport_players[sport]
            print("%s(%d,%d)" % (department, teams, spares), end = "")
    print()