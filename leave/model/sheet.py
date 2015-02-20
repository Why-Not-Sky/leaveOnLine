__author__ = 'sky_wu'

from datetime import datetime, timedelta
from leave.model.section import Section
import re


class TimeSection:
    def __init__(self, st='08:30', et='17:30', so=0, eo=0):
        self.start_time = st  # '0830'stime[0:2]+ ':' + stime[2:4]
        self.end_time = et  # datetime(1, 1, 1, int(etime[0:2]), int(etime[2:4]))
        self.start_offset = so  # -1:previous day(23:00~) /0:today /1:next day (00:00~)
        self.end_offset = eo  # -1:previous day(23:00~) /0:today /1:next day (00:00~)

    def sheet_time(self, str_dte):
        res = Section(None, None)
        res.start_point = datetime.strptime(str_dte + ' ' + self.start_time, "%Y/%m/%d %H:%M") + timedelta(
            days=self.start_offset)
        res.end_point = datetime.strptime(str_dte + ' ' + self.end_time, "%Y/%m/%d %H:%M") + + timedelta(
            days=self.end_offset)
        return (res)

class Sheet:
    # Date = datetime.strptime("10/10/11", "%m/%d/%y")
    def __init__(self, sid):
        self.sheet_id = sid
        self.sheet_name = 'daylight'
        self.work_section = TimeSection()
        self.rest_sections = []  # list of TimeSection()

def load_sheet(sid, sh:Sheet):
    d = sheets[sid]
    sh.__dict__ = d  # use dictionary to assign value directly, error caused by timeSection methods
    # for k in d.keys(): sh.__dict__[k]=d[k]     #type of work_section changed from TimeScrtion to dict


sheets = {
      'N': dict(sheet_id='N', sheet_name='normal', work_section=TimeSection('08:30', '17:30', 0, 0)
                    , rest_sections=[TimeSection('12:00', '13:00', 0, 0)])
    , 'L': dict(sheet_id='L', sheet_name='light', work_section=TimeSection('08:00', '16:00', 0, 0)
                , rest_sections=[TimeSection('12:00', '12:30', 0, 0)])
    , 'M': dict(sheet_id='M', sheet_name='moon', work_section=TimeSection('16:00', '00:00', 0, 1)
                , rest_sections=[TimeSection('20:00', '20:30', 0, 0)])
    , 'S': dict(sheet_id='S', sheet_name='star', work_section=TimeSection('00:00', '08:00', 1, 1)
                , rest_sections=[TimeSection('04:00', '04:30', 1, 1)])
    , 'C1': dict(sheet_id='C1', sheet_name='12H1', work_section=TimeSection('08:00', '20:00', 0, 0)
                , rest_sections=[TimeSection('11:30', '12:00', 0, 0), TimeSection('16:00', '16:30', 0, 0)])
    , 'C2': dict(sheet_id='C2', sheet_name='12H2', work_section=TimeSection('20:00', '08:00', 0, 1)
                 , rest_sections=[TimeSection('23:30', '00:00', 0, 1), TimeSection('04:00', '04:30', 1, 1)])
}

sheets_dict = {
      'N': dict(sheet_id='N', sheet_name='normal',
              work_section=dict(start_time='08:30', end_time='17:30', start_offset=0, end_offset=0))
    , 'L': dict(sheet_id='L', sheet_name='light',
                work_section=dict(start_time='08:00', end_time='16:00', start_offset=0, end_offset=0))
    , 'M': dict(sheet_id='M', sheet_name='moon',
                work_section=dict(start_time='16:00', end_time='00:00', start_offset=0, end_offset=1))
    , 'S': dict(sheet_id='S', sheet_name='star',
                work_section=dict(start_time='00:00', end_time='08:00', start_offset=1, end_offset=1))
}

sheets_tuple = [('N', 'normal', '08:30', '17:30', 0, 0)
    , ('L', 'light', '08:30', '17:30', 0, 0)
    , ('M', 'moon', '08:30', '17:30', 0, 0)
    , ('S', 'star', '08:30', '17:30', 0, 0)]

DEBUG = False

if __name__ == '__main__':
    work_day = '2015/01/01'

    tw = TimeSection()
    #print(tw.sheet_time(work_day).dump())

    s = Sheet('A')
    if DEBUG:
        print(s.work_section.sheet_time(work_day).dump())
        for r in s.rest_sections: print('\t rest_sections.%d=' % s.rest_sections.index(r), r.sheet_time(work_day).dump())

    #load each class and dump
    for sid in sheets.keys():
        load_sheet(sid, s)
        print('\n' if (list(sheets.keys()).index(sid) > 0) else '', s.work_section.sheet_time(work_day).dump())
        for r in s.rest_sections: print('\t rest_sections.%d=' % s.rest_sections.index(r), r.sheet_time(work_day).dump())



