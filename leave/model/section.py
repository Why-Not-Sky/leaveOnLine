from datetime import datetime

class Section:
    def __init__(self, sdt, edt):
        self.start_point=sdt
        self.end_point=edt

    def display(self):
        if (self is not None):
            return ('(' + self.start_point.strftime("%Y/%m/%d %H:%M") + "--> " + self.end_point.strftime("%Y/%m/%d %H:%M") + ')')

    def overlap(self, co):
        #if any overlap
        if (self.start_point < co.end_point and self.end_point > co.start_point):
            res=Section(None, None) #side effect if use co directly
            res.start_point=max(self.start_point, co.start_point)
            res.end_point=min(self.end_point, co.end_point)
            return (res)

    def distance(self):  #datetime.timedelta
        #to-do: use type to decide return type, return hours first
        return((self.end_point-self.start_point).seconds/3600)

    def dump(self):
        if (self is not None):
            return(self.display() + ':' + str(self.distance())+' hours')

if __name__ == "__main__":
    # Create an object:
    w = Section(datetime(2015,1,1,8,30), datetime(2015,1,1,12,00)) #work1
    lo = Section(datetime(2015,1,1,10,30), datetime(2015,1,1,12,00)) #overlap
    lc = Section(datetime(2015,1,1,8,30), datetime(2015,1,1,17,30)) #cover
    ln = Section(datetime(2015,1,1,12,30), datetime(2015,1,1,14,00)) #none

    print('w1=', w.dump())

    lo1=lo.overlap(w)
    #print (lo.dump, 'overlap w=', lo1.dump() if lo1 is not None)
    print (lo.dump(), 'overlap w=')
    if lo1 is not None: print('\t', lo1.dump())

    lc1=lc.overlap(w)
    print (lc.dump(), 'contain w=')
    if lc1 is not None: print('\t', lc1.dump())

    ln1=ln.overlap(w)
    print (ln.dump(), 'overlap w=')
    if ln1 is not None: print('\t', ln1.dump())
    else: print('\t', 'None')
