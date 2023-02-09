def number_name(n):
    l = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    return l[int(n)]
    
n = input()
print(n, '-->', number_name(n))