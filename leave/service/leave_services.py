__author__ = 'sky_wu'
"""
define the servics facade of leave
isLeaveOverlap: 某時段是否已有請假?
getLeaveList: 取得某段時間的請假清單
calculateLeaveHour:計算請假時數
getPlannedWorkSection: 取得某段時間(日)的應工作時段
getDesiredWorkSection: 取得某段時間(日)的應工作時段
getActualWorkSection:取得實際工作時段
getPlannedWorkSheet:
getCalendar:
"""
from model.section import *

class leave_services:
    def __init__(self):
      pass

    def is_leave_validate(self, applicant_id, from_date, to_date):
        pass

    def is_leave_duplicated(self, applicant_id, from_date, to_date):
        return(False)

    def calculate_leave(self, applicant_id, from_date, to_date):
        #return hours first
        return(3.5)

class agent_services:
    def __init__(self):
        pass

    def get_default_agent(self, applicant_id):
        pass

    def get_agents(self, applicant_id):
        pass

if __name__ == '__main__':
    w1 = Section(datetime(2015,1,1,8,30), datetime(2015,1,1,12,00)) #work1
    w2 = Section(datetime(2015,1,1,13,00), datetime(2015,1,1,17,30)) #work2
    w3 = Section(datetime(2015,1,2,8,30), datetime(2015,1,2,12,00)) #work1

    lev = Section(datetime(2015,1,1,10,30), datetime(2015,1,1,16,00)) #leave answer: 4.5hour

    work=[w1,w2,w3]   #list of section
    for w in work: print('w%d=' % work.index(w), w.dump())

    ws=[]    #print (len(ws))
    for l in work:
        seg=lev.intersection(l)
        if seg is not None: ws.append(seg)
    for w in ws: print('ws%d=' % ws.index(w), w.dump())
    print('ws=', sum(x.distance() for x in ws))

    ws1=[lev.intersection(w) for w in work] # if lev.intersection(w) is not None]
    for w in ws1:
        if w is not None:print('ws1.%d=' % ws1.index(w), w.dump())

    lev_hours = 0.0
    for sec in ws1:
        if sec is not None: lev_hours += sec.distance()
    #assert isinstance(lev_hours, object)
    print('ws1=', lev_hours)

    #use map
    ws2=list(map(lambda w:lev.intersection(w) , work))
    for seg in ws2: #pass
        if seg is not None: print('w2.%d intersection =' % ws2.index(seg), seg.dump())
    print('ws2=', sum(x.distance() for x in ws if x is not None))

    #calculate the intersection first, then filter the none
    ws3=list(filter(lambda x: x is not None, map(lambda w:lev.intersection(w) , work)))
    for w in ws3: print('ws3.%d=' % ws3.index(w), w.dump())

    #reduce(lambda a,b: a*b, numbers) --> python 2
    lev_hour = functools.reduce(lambda a,b: a.distance()+b.distance(), ws3)
    #lev_hour = (lambda w: w.distance()+ , ws3)
    print('ws3=', lev_hour) #.distance())