__author__ = 'sky_wu'

from datetime import datetime
from leave.model.section import Section
from leave.model.sheet import Sheet


#personal's schedule to work
class Schedule:
    def __init__(self, sdate:datetime, sid):
        self.work_date=sdate
        self.sheet_time=Sheet(sid) #sheet time definition
        self.work_start = sdate         #from 08:00~
        self.end_time = sdate + 1