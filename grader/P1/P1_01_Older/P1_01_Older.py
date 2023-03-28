name_months = ["January","February","March","April","May","June","July","August","September","October","November","December"]
name1, name_month1, raw_date1, raw_year1 = input().split()
name2, name_month2, raw_date2, raw_year2 = input().split()
month1 = name_months.index(name_month1)
month2 = name_months.index(name_month2)
date1 = int(raw_date1[:-1])
date2 = int(raw_date2[:-1])
year1 = int(raw_year1)
year2 = int(raw_year2)

if year1 < year2:
    print(name1)
elif year2 < year1:
    print(name2)
else:
    if month1 < month2:
        print(name1)
    elif month2 < month1:
        print(name2)
    else:
        if date1 < date2:
            print(name1)
        elif date2 < date1:
            print(name2)
        else:
            print(name1, name2)
            