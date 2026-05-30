def year_leap (year):
    if year%400==0:
        return True
    elif year%100==0:
        return False
    elif year%4==0:
        return True
    else:
        False

def day_in_month(year,month):
    month_days=[31,28,31,30,31,30,31,31,30,31,30,31]
    if year_leap(year) is True and month==2:
        return 29
    return month_days[month-1]







year=int(input("what year would you like to check??\n"))
month=int(input("what month you would like to check??\n"))
days=day_in_month(year,month)
print(days)