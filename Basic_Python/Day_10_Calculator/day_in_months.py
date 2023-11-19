
def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
            #    print("Leap year")
               return True
            else:
            #    print("Not Leap year")
               return False
        else:
            # print("Leap year")
            return True
    else:
        # print("Not Leap year")
        return False


def days_in_month(year, month):
    month_days =[31,28,31,30,31,30,31,31,30,31,30,30]

    #Better answer, can remove all other code
    #if month ==2 and is_leap(year):
    # return 29
    #else:
    # return month_days[month-1]
    
    """this is my code (doc string)"""
    month_num = month-1 #array start from 0.
    year_status = is_leap(year)    
    if year_status == True and month_num == 2:
        month_days[month_num] = 29

    return f"{month_days[month_num]}"
    """"""

year = int(input())
month = int(input())
days = days_in_month(year, month)
print(days)