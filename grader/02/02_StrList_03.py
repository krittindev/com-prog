def number_name_month(n):
    l = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    return l[int(n)-1]
    
day, month, year = input().split('/')
print(number_name_month(month), day + ',', year)