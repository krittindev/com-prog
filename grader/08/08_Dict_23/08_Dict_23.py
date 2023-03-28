name_phone = {}
phone_name = {}
n = int(input().strip())
for _ in range(n):
    first_name, last_name, phone = input().strip().split()
    name_phone[first_name + ' ' + last_name] = phone
    phone_name[phone] = first_name + ' ' + last_name
m = int(input().strip())
for _ in range(m):
    find = input().strip()
    found = ''
    if find in name_phone:
        found = name_phone[find]
    elif find in phone_name:
        found = phone_name[find]
    else:
        found = 'Not found'
    print(find + ' --> ' + found)
