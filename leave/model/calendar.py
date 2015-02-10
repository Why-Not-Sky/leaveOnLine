from datetime import datetime, timedelta
from self_datetime import get_calendar_date

class Calendar:
    except_date=[datetime(2015, 2, i) for i in range(18, 25)]  #not include 25
    #test tuples
    #except_date=(datetime(2015, 2, i) for i in range(18, 25))  #not include 25
    except_number=(1,2,3)

    def __init__(self, w_year, w_month=0):
        self.work_year = w_year
        self.work_month = w_month
        self.calendar_date = get_calendar_date(w_year, w_month)
        self.work_date = [d for d in self.calendar_date if (d.weekday() not in [5, 6]) and (d not in self.except_date)]

    def work_date(self):
        pass

    def work_time(self):
        pass

if __name__ == "__main__":
    work_year = 2015
    work_month = 2

    wc = Calendar(work_year, work_month)
    for d in wc.work_date: print(d.strftime("%Y/%m/%d"), d.weekday())
    for d in wc.except_date: print(d.strftime("%Y/%m/%d"))
    #print(wc.except_date)
    print(wc.except_number)

"""
    calendar_date = get_calendar_date(work_year, work_month)
    for d in calendar_date: print(d.strftime("%Y/%m/%d"), d.weekday())

    #squares = [number*number for number in numbers if number < 4]
    #datetime.datetime(2015, 2, 8).weekday()
    #Monday == 0 ... Sunday == 6
    work_date=[d for d in calendar_date if d.weekday() not in [5, 6]] # and d.year==work_year]
    for d in work_date: print(d.strftime("%Y/%m/%d"), d.weekday())

    work_date=filter(lambda x: x.weekday() not in [5, 6], calendar_date)
    for d in work_date: print(d.strftime("%Y/%m/%d"), d.weekday())
"""





