from datetime import datetime
import functools
#https://docs.python.org/3.0/library/time.html#time.strptime

class Section:
    def __init__(self, sdt, edt):
        self.start_point=sdt
        self.end_point=edt

    def display(self):
        if (self is not None):
          return ('(' + self.start_point.strftime("%Y/%m/%d %H:%M") + "--> " + self.end_point.strftime("%Y/%m/%d %H:%M") + ')')

    def overlap(self, co):
        #return (if (self.star_point < co.start_point) and (self.end_point>co.start_point))
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
    w1 = Section(datetime(2015,1,1,8,30), datetime(2015,1,1,12,00)) #work1
    w2 = Section(datetime(2015,1,1,13,00), datetime(2015,1,1,17,30)) #work2
    w3 = Section(datetime(2015,1,2,8,30), datetime(2015,1,2,12,00)) #work1

    lev = Section(datetime(2015,1,1,10,30), datetime(2015,1,1,16,00)) #leave answer: 4.5hour

    work=[w1,w2,w3]   #list of section
    for w in work: print('w%d=' % work.index(w), w.dump())









