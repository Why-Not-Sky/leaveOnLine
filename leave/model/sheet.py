__author__ = 'sky_wu'

from datetime import datetime, timedelta
from leave.model.section import Section
import re

sheets = {'N':dict(sheet_id='N', sheet_name='normal', start_time='08:30', end_time='17:30', start_offset=0, end_offset=0)
        , 'L':dict(sheet_id='L', sheet_name='light', start_time='08:00', end_time='16:00', start_offset=0, end_offset=0)
        , 'M':dict(sheet_id='M', sheet_name='moon', start_time='16:00', end_time='00:00', start_offset=0, end_offset=1)
        , 'S':dict(sheet_id='S', sheet_name='star', start_time='00:00', end_time='08:00', start_offset=1, end_offset=1)}

sheets_tuple = [('N', 'normal', '08:30', '17:30', 0, 0)
            , ('L', 'light', '08:30', '17:30', 0, 0)
            , ('M', 'moon', '08:30', '17:30', 0, 0)
            , ('S', 'star', '08:30', '17:30', 0, 0)]

class Sheet:
    #Date = datetime.strptime("10/10/11", "%m/%d/%y")
    def __init__(self, sid):
        self.sheet_id=sid
        self.sheet_name='daylight'
        self.start_time= '08:30'        #'0830'stime[0:2]+ ':' + stime[2:4]
        self.end_time= '17:30'          #datetime(1, 1, 1, int(etime[0:2]), int(etime[2:4]))
        self.start_offset=0   #-1:previous day(23:00~) /0:today /1:next day (00:00~)
        self.end_offset=0   #-1:previous day(23:00~) /0:today /1:next day (00:00~)

    def sheet_time(self, str_dte):
        res= Section(None, None)
        res.start_point= datetime.strptime(str_dte + ' '  + self.start_time, "%Y/%m/%d %H:%M") + timedelta(days=self.start_offset)
        res.end_point= datetime.strptime(str_dte + ' '  + self.end_time, "%Y/%m/%d %H:%M") +  + timedelta(days=self.end_offset)
        return(res)

def load_sheet(sid, sh:Sheet):
    d=sheets[sid]
    sh.__dict__ = d  #use dictionary to assign value directly

if __name__ == '__main__':
    work_day='2015/01/01'

    s = Sheet(None)
    load_sheet('L', s)
    print(s.sheet_time(work_day).dump())

    for sid in sheets.keys():
        load_sheet(sid, s)
        print(s.sheet_time(work_day).dump())



