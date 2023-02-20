names_nicknames = [
    ['Robert', 'Dick'], 
    ['William', 'Bill'], 
    ['James', 'Jim'], 
    ['John', 'Jack'], 
    ['Margaret', 'Peggy'], 
    ['Edward', 'Ed'], 
    ['Sarah', 'Sally'], 
    ['Andrew', 'Andy'], 
    ['Anthony', 'Tony'], 
    ['Deborah', 'Debbie']
]
names = [e[0] for e in names_nicknames]
nicknames  = [e[1] for e in names_nicknames]

n = int(input().strip())
for _ in range(n):
    name = input().strip()
    if name in names:
        print(nicknames[names.index(name)])
    elif name in nicknames:
        print(names[nicknames.index(name)])
    else:
        print('Not found')