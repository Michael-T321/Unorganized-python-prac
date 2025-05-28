import datetime # imports the datetime

print (datetime.date.now())

# datetime is a module within python where datetime refers to the date class inside the datetime module.
# This class represents a calendar date (year, month, and day) without any time info.
# .today() is a class method of date that returns the current local date (based on your system’s time zone).

# datetime.datetime.today() -- .today -- No time zone support (can't change time zone)
# datetime.datetime.now() --  .now -- Supports time zone (can change time zone)
# datetime.date.today() -- prints, year, month, and day
# datetime.datetime.now() --  prints year, month, day, hour, second, etc

today = datetime.date.today()

year = today.year
month = today.month
day = today.day

print("Year:", year)
print("Month:", month)
print("Day:", day)