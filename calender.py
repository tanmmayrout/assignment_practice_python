# Importing the calendar module
import calendar

# Function returns a string, so we split the string by spaces and convert them into integers
month, day, year = map(int, input("Enter month, day, and year: ").split())

print(calendar.day_name[calendar.weekday(year, month, day)].upper())  # Calender library functions
