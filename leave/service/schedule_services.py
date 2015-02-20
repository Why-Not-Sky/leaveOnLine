__author__ = 'sky_wu'

from model.schedule import *

class ScheduleServices:
    def getSchedule(self, pid, sdate, edate=None):
        self.schedule=[]
        while (sdate < edate):
            self.schedule.append(Schedule(sdate))
            sdate += 1

