#First assignment for WEEE entry test - Lorenzo Callegari
from datetime import date
import datetime, calendar, sys

def isRealDate(in_date):
    try:
        datetime.datetime.strptime(in_date, '%d/%m/%Y')
    except ValueError:
        print("Incorrect data format, should be DD/MM/YYYY")
        exit()

in_date = sys.argv[1]

isRealDate(in_date)
dayName = calendar.day_name[date(int(in_date[6:10]), int(in_date[3:5]), int(in_date[0:2])).weekday()]
print("\nThe inserted date " + in_date + " is on a " + dayName)

daysFromin_date = str(abs((datetime.datetime(int(in_date[6:10]), int(in_date[3:5]), int(in_date[0:2])) - datetime.datetime.now()).days))
print(daysFromin_date + " days will pass or have passed from " + in_date)
