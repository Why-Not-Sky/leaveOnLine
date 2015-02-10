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
class leave_services:
    def __init__(self):
      pass

    def is_leave_validate(self, applicant_id, from_date, to_date):
        pass

    def is_leave_overlap(self, applicant_id, from_date, to_date):
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