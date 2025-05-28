# Date: 4/2/25
# Create a small profile using a string, int, float, and boolean. This will take the students name, age, and GPA and determine whether
# are in good academic standing or not.
# 

import datetime

first_name = input("Students first name: ") # String value for first name
last_name = input("Students last name: ") # string value for last name
GPA = float(input("Enter Students GPA: ")) # boolean value GPA


month_born = int(input("Enter the month you were born (1-12): ")) # input users birth month
day_born =  int(input("Enter the day of the month you were born (1-31): ")) # input users birth day
year_born = int(input("Enter the year you were born : ")) # input users birth year

month_count = month_born # creates another variable with the same value as month_born
today = datetime.date.today() # creates a varaible equal to the date today

year = today.year # create variable that has the currect year
month = today.month # creates a variable that has the current month
day = today.day # creates a variable that has the current day


age_year = year - year_born # calculates the age in years
age_month = month - month_born # calculates the number of months on top of year

if month_born  == month:
    days = 0 # sets number of days set to 0
    if day_born == day:
        print(f"Today is your birthday! You are exactly {age_year} years old!")
    elif day_born <= day:
        age_day = day - day_born
        print(f"You are exatly {age_year} years and {age_day} days old!")
    else:
        age_year = age_year - 1
        age_day = (day_born - day)
        print(f"You are {age_year} years old and there are {age_day} days till your birthday")

elif month_born < month:
        if month_born == 2:
            days = 28 - day_born
        elif month_born in [4, 6, 9, 11]:
            days = 30 - day_born
        elif month_born in [1, 3, 5, 7, 8, 10, 12]:
            days = 31 - day_born
        month_count += 1
        while month_count < month:
            if month_count in [2]:
                days = days + 28
                month_count += 1
            elif month_count in [4, 6, 9, 11]:
                days = days + 30
                month_count += 1
            elif month_count in [1, 3, 5, 7, 8, 10, 12]:
                days =  days + 31
                month_count += 1
        else: 
            days =  days + day
            print(f"You are exactly {age_year} years and {days} days old")


elif month_born > month: 
        age_year -= 1
        
        if month == 2:
            days = 28 - day
        elif month in [4, 6, 9, 11]:
            days = 30 - day
        elif month_born in [1, 3, 5, 7, 8, 10, 12]:
            days = 31 - day
        days = days + day_born
        month_count -= 1
        while month_count > month:
            if month_count in [2]:
                days = days + 28
                month_count -= 1
            elif month_count in [4, 6, 9, 11]:
                days = days + 30
                month_count -= 1
            elif month_count in [1, 3, 5, 7, 8, 10, 12]:
                days =  days + 31
                month_count -= 1
        else:
            days = 365 - days
       
print(f"Students name: {first_name} {last_name}") # prints student first and last name
print(f"Student was born on {month_born}/{day_born}/{year_born}")
print(f"Student is exactly {age_year} years and {days} days old")











