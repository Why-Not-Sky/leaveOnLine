__author__ = 'sky_wu'

import unittest

#from model.section import *
from section import *


class TestSection(unittest.TestCase):

    def test_leave_intersection(self):
        w = Section(datetime(2015,1,1,8,30), datetime(2015,1,1,12,00))

    # happy path: 1 intersection
    # self.start_point < co.end_point and self.end_point > co.start_point
        l = Section(datetime(2015,1,1,8,30), datetime(2015,1,1,12,00)) #intersection
        l1=l.intersection(w)
        self.assertEqual((l1.start_point, l1.end_point), (datetime(2015,1,1,8,30), datetime(2015,1,1,12,00)))
        self.assertEqual(l1.distance(), 3.5)

    #def test_leave_within_work(self):
        #self.start_point < co.end_point and self.end_point > co.start_point
        #w = Section(datetime(2015,1,1,8,30), datetime(2015,1,1,12,00))
        l = Section(datetime(2015,1,1,8,30), datetime(2015,1,1,11,00)) #with in worktime

        l1=l.intersection(w)
        self.assertEqual(l1.distance(), 1.5)

    #self.start_point < co.end_point and self.end_point > co.start_point
    def test_leave_cove_work(self):
        w = Section(datetime(2015,1,1,8,30), datetime(2015,1,1,12,00))
        l = Section(datetime(2015,1,1,8,30), datetime(2015,1,1,14,00)) #cover

        l1=l.intersection(w)
        self.assertEqual(l1.distance(), 3.5)

    #(self.start_point < co.end_point==True) (self.end_point > co.start_point=False)
    def test_leave_above_work(self):
        w = Section(datetime(2015,1,1,8,30), datetime(2015,1,1,12,00))
        l = Section(datetime(2015,1,1,13,30), datetime(2015,1,1,16,00)) #none

        l1=l.intersection(w)
        self.assertEqual(l1, None)

    #(self.start_point < co.end_point==True) (self.end_point > co.start_point=False)
    def test_leave_below_work(self):
        w = Section(datetime(2015,1,1,8,30), datetime(2015,1,1,12,00))
        l = Section(datetime(2014,12,31, 14, 30), datetime(2014,12,31,17,30)) #none

        l1=l.intersection(w)
        self.assertEqual(l1, None)

    #test difference method
    def test_work_difference(self):
        w = Section(datetime(2015,1,1,8,30), datetime(2015,1,1,12,00))
        l = Section(datetime(2015,1,1,10,30), datetime(2015,1,1,15,00)) #intersection

        wlist=w.difference(l)
        self.assertEqual((wlist[0].start_point, wlist[0].end_point), (datetime(2015,1,1,8,30), datetime(2015,1,1,10,30)))
        self.assertEqual(wlist[0].distance(), 2)

    def test_work_divide2section(self):
        w = Section(datetime(2015,1,1,8,30), datetime(2015,1,1,12,00))
        l = Section(datetime(2015,1,1,9,30), datetime(2015,1,1,11,00)) #with in worktime

        wlist=w.difference(l)
        self.assertEqual((wlist[0].start_point, wlist[0].end_point), (datetime(2015,1,1,8,30), datetime(2015,1,1,9,30)))
        self.assertEqual((wlist[1].start_point, wlist[1].end_point), (datetime(2015,1,1,11,00), datetime(2015,1,1,12,00)))

    def test_work_none(self):
        w = Section(datetime(2015,1,1,8,30), datetime(2015,1,1,12,00))
        l = Section(datetime(2015,1,1,8,30), datetime(2015,1,1,14,00)) #cover

        wlist=w.difference(l)
        self.assertEqual(wlist, []) #None

if __name__ == '__main__':
    unittest.main()

