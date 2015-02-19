__author__ = 'sky_wu'

import unittest
from datetime import datetime
from section import Section

class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, True)

    #self.start_point < co.end_point and self.end_point > co.start_point
    def test_intersection(self):
        w = Section(datetime(2015,1,1,8,30), datetime(2015,1,1,12,00))
        l = Section(datetime(2015,1,1,10,30), datetime(2015,1,1,15,00)) #intersection

        l1=l.intersection(w)
        self.assertEqual((l1.start_point, l1.end_point), (datetime(2015,1,1,10,30), datetime(2015,1,1,12,00)))
        self.assertEqual(l1.distance(), 1.5)

    #self.start_point < co.end_point and self.end_point > co.start_point
    def test_contain(self):
        w = Section(datetime(2015,1,1,8,30), datetime(2015,1,1,12,00))
        l = Section(datetime(2015,1,1,9,30), datetime(2015,1,1,11,00)) #cover

        l1=l.intersection(w)
        self.assertEqual(l1.distance(), 1.5)

    #self.start_point < co.end_point and self.end_point > co.start_point
    def test_cover(self):
        w = Section(datetime(2015,1,1,8,30), datetime(2015,1,1,12,00))
        l = Section(datetime(2015,1,1,8,30), datetime(2015,1,1,14,00)) #cover

        l1=l.intersection(w)
        self.assertEqual(l1.distance(), 3.5)

    #(self.start_point < co.end_point==True) (self.end_point > co.start_point=False)
    def test_none_above(self):
        w = Section(datetime(2015,1,1,8,30), datetime(2015,1,1,12,00))
        l = Section(datetime(2015,1,1,13,30), datetime(2015,1,1,16,00)) #none

        l1=l.intersection(w)
        self.assertEqual(l1, None)

    #(self.start_point < co.end_point==True) (self.end_point > co.start_point=False)
    def test_none_below(self):
        w = Section(datetime(2015,1,1,8,30), datetime(2015,1,1,12,00))
        l = Section(datetime(2014,12,31, 14, 30), datetime(2014,12,31,17,30)) #none

        l1=l.intersection(w)
        self.assertEqual(l1, None)

if __name__ == '__main__':
    unittest.main()

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