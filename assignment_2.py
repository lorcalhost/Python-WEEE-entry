#Second assignment for WEEE entry test - Lorenzo Callegari
from datetime import date
import datetime
import calendar
import sys


class InvalidDateError(Exception):
    def __init__(self, code):
        self.code = code


class NoArgumentsError(Exception):
    def __init__(self, code):
        self.code = code


def is_real_date(in_date):
    try:
        datetime.datetime.strptime(in_date, '%d/%m/%Y')
    except ValueError:
        raise InvalidDateError(
            "[{}] is an invalid date format, should be DD/MM/YYYY".format(sys.argv[1]))


def enough_arguments():
    if len(sys.argv) < 2:
        raise NoArgumentsError("Not enough arguments given")


enough_arguments()
# Checking for badly written input, in case it is detected, InvalidDateError is raised
is_real_date(sys.argv[1])
day = int(sys.argv[1][0:2])
month = int(sys.argv[1][3:5])
year = int(sys.argv[1][6:10])


day_name = calendar.day_name[date(year, month, day).weekday()]
print("The inserted date {} is on a {}".format(sys.argv[1], day_name))

days_from_date = (datetime.datetime(year, month, day) -
                  datetime.datetime.now()).days
if days_from_date < 0:
    print("{} days have passed from {}".format(-days_from_date, sys.argv[1]))
else:
    print("{} days will pass before {}".format(days_from_date, sys.argv[1]))
