__author__ = 'sky_wu'
from datetime import datetime, timedelta


def add_months(mydate, nm):
    current = datetime(mydate.year, mydate.month, 1)
    return (datetime(mydate.year + int((mydate.month + nm) / 12), (mydate.month + nm) % 12, 1))


def days_of_month(mydate):
    current = datetime(mydate.year, mydate.month, 1)
    next_month = datetime(mydate.year + int((mydate.month + 1) / 12), (mydate.month + 1) % 12, 1)
    return ((next_month - current).days)


def get_calendar_date(wy, wm=0):
    if wm == 0:
        wm = 1
        days_add = (wy % 400 == 0 or (wy % 4 == 0 and wy % 100 != 0)) and 366 or 365
    else:
        days_add = days_of_month(datetime(wy, wm, 1))

    date_begin = datetime(wy, wm, 1)

    return ([date_begin + timedelta(days=i) for i in range(days_add)])  # if (date_begin + timedelta(days=i)).year==wy])


if __name__ == "__main__":
    work_year = 2015
    work_month = 2
    # datetime.date(2015, 1, 1) + timedelta(days=1)
    print (days_of_month(datetime(work_year, work_month, 1)))
    print (add_months(datetime(work_year, work_month, 1), 2))
    pass

    calendar_date = get_calendar_date(work_year, work_month)
    for d in calendar_date: print(d.strftime("%Y/%m/%d"), d.weekday())