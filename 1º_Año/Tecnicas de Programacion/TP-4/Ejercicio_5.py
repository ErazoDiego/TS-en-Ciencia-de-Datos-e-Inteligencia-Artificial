def is_year_leap(year):
    if year < 1582:
        print("No dentro del período del calendario Gregoriano.")
    else:
        if year % 4 != 0:
            return False
        elif year % 100 != 0:
            return True
        elif year % 400 != 0:
            return False
        else:
            return True


def days_in_month(year, month):
    if month == 2:
        if is_year_leap(year) == True:
            return 29
        else:
            return 28
    elif month in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    else:
        return 30


def day_of_year(year, month, day):
    cont_days = 0
    for i in range(1, month):
        days = days_in_month(year, i)
        if days == None:
            return None
        cont_days += days
    days = days_in_month(year, month)
    if day >= 1 and day <= days:
        return cont_days
    else:
        return None


print(day_of_year(2022, 12, 31))
