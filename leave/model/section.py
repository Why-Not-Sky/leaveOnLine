from datetime import datetime


class Section:
    def __init__(self, sdt, edt):
        self.start_point = sdt
        self.end_point = edt

    def intersection(self, co):
        """need to define if intersect at then end point
        :self:         |-----------|
        :param co: |----------|
        :return:       |------|
        """
        if (self.start_point < co.end_point and self.end_point > co.start_point):
            res = Section(None, None)  # side effect if use co directly
            res.start_point = max(self.start_point, co.start_point)
            res.end_point = min(self.end_point, co.end_point)
            return (res)

    def difference(self, co):
        """
        :self:     |---------------|
        :param co:     |------|
        :return:   |---|      |----|
        """
        res = []
        if (self.start_point < co.end_point and self.end_point > co.start_point):
            if (self.start_point < co.start_point): res.append(Section(self.start_point, co.start_point))
            if (self.end_point > co.end_point): res.append(Section(co.end_point, self.end_point))
            return (res)
        else:  # res.append(res.append(self))  #not work
            res.append(self)
            return (res)  #no intersection return self

    def distance(self):  # datetime.timedelta
        #to-do: use type to decide return type, return hours first
        return ((self.end_point - self.start_point).seconds / 3600)

    def display(self):
        if (self is not None):
            return ('(' + self.start_point.strftime("%Y/%m/%d %H:%M") + "--> " + self.end_point.strftime(
                "%Y/%m/%d %H:%M") + ')')

    def dump(self):
        if (self is not None):
            return (self.display() + ':' + str(self.distance()) + ' hours')


if __name__ == "__main__":
    # Create an object:
    work_sheet = Section(datetime(2015, 1, 1, 8, 30), datetime(2015, 1, 1, 17, 30))  # work1
    rest_time = Section(datetime(2015, 1, 1, 12, 00), datetime(2015, 1, 1, 13, 00))  # rest time
    work_time = work_sheet.difference(rest_time)
    for w in work_time: print('work_time.%d=' % work_time.index(w), w.dump())

    w = work_time[0]

    lo = Section(datetime(2015, 1, 1, 10, 30), datetime(2015, 1, 1, 12, 00))  # intersection
    lc = Section(datetime(2015, 1, 1, 8, 30), datetime(2015, 1, 1, 17, 30))  # cover
    ln = Section(datetime(2015, 1, 2, 12, 30), datetime(2015, 1, 2, 14, 00))  # none
    lc2 = Section(datetime(2015, 1, 1, 10, 30), datetime(2015, 1, 1, 11, 30))  # 2 card time section

    wlist = w.difference(lc2)
    for w in wlist: print('wlist.%d=' % wlist.index(w), w.dump())

    lo1 = lo.intersection(w)
    # print (lo.dump, 'intersection w=', lo1.dump() if lo1 is not None)
    print(lo.dump(), 'intersection w=',
          lo1.dump() if lo1 is not None else None)  #'Test is True' if test else 'Test is False'

    lc1 = lc.intersection(w)
    print(lc.dump(), 'contain w=', lc1.dump() if lc1 is not None else None)
    #if lc1 is not None: print('\t', lc1.dump())

    ln1 = ln.intersection(w)
    print(ln.dump(), 'intersection w=', ln1.dump() if ln1 is not None else None)
    #if ln1 is not None: print('\t', ln1.dump())
    #else: print('\t', 'None')


