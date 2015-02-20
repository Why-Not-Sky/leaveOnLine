__author__ = 'sky_wu'

import unittest
from datetime import datetime
from leave.model.section import Section
# from section import *

class TestSection(unittest.TestCase):
    def test_intersection(self):
        w = Section(datetime(2015, 1, 1, 8, 30), datetime(2015, 1, 1, 12, 00))

        #self.start_point < co.end_point and self.end_point > co.start_point
        #happy: full
        #def test_leave_intersect_work(self):
        l = Section(datetime(2015, 1, 1, 8, 30), datetime(2015, 1, 1, 12, 00))  #intersection
        l1 = l.intersection(w)
        self.assertEqual((l1.start_point, l1.end_point), (datetime(2015, 1, 1, 8, 30), datetime(2015, 1, 1, 12, 00)))

        #self.start_point < co.end_point and self.end_point > co.start_point
        #happy: front
        #def test_leave_within_work_front(self):
        l = Section(datetime(2015, 1, 1, 8, 30), datetime(2015, 1, 1, 11, 00))  #with in worktime

        l1 = l.intersection(w)
        self.assertEqual((l1.start_point, l1.end_point), (datetime(2015, 1, 1, 8, 30), datetime(2015, 1, 1, 11, 00)))

        #self.start_point < co.end_point and self.end_point > co.start_point
        #happy: middle
        #def test_leave_within_work_middle(self):
        l = Section(datetime(2015, 1, 1, 9, 30), datetime(2015, 1, 1, 11, 00))  #with in worktime

        l1 = l.intersection(w)
        self.assertEqual((l1.start_point, l1.end_point), (datetime(2015, 1, 1, 9, 30), datetime(2015, 1, 1, 11, 00)))

        #self.start_point < co.end_point and self.end_point > co.start_point
        #happy: full & over
        #def test_leave_cover_work(self):
        l = Section(datetime(2015, 1, 1, 8, 30), datetime(2015, 1, 1, 14, 00))  #cover

        l1 = l.intersection(w)
        self.assertEqual((l1.start_point, l1.end_point), (datetime(2015, 1, 1, 8, 30), datetime(2015, 1, 1, 12, 00)))

        #(self.start_point < co.end_point==False) (self.end_point > co.start_point=True)
        #alternative: none
        #def test_leave_above_work(self):
        l = Section(datetime(2015, 1, 1, 13, 30), datetime(2015, 1, 1, 16, 00))  #none

        l1 = l.intersection(w)
        self.assertEqual(l1, None)

        #(self.start_point < co.end_point==True) (self.end_point > co.start_point=False)
        #alternative: none
        #def test_leave_below_work(self):
        w = Section(datetime(2015, 1, 1, 8, 30), datetime(2015, 1, 1, 12, 00))
        l = Section(datetime(2014, 12, 31, 14, 30), datetime(2014, 12, 31, 17, 30))  #none

        l1 = l.intersection(w)
        self.assertEqual(l1, None)

    #test difference method
    #self.start_point < co.end_point and self.end_point > co.start_point
    #happy: full
    #def test_difference_full(self):
    def test_difference(self):
        w = Section(datetime(2015, 1, 1, 8, 30), datetime(2015, 1, 1, 12, 00))

        l = Section(datetime(2015, 1, 1, 8, 30), datetime(2015, 1, 1, 12, 00))  #intersection
        wlist = w.difference(l)
        self.assertEqual(wlist, [])  #None

        #self.start_point < co.end_point and self.end_point > co.start_point
        #happy: front
        #def test_difference_front(self):
        l = Section(datetime(2015, 1, 1, 8, 30), datetime(2015, 1, 1, 11, 00))  #intersection

        wlist = w.difference(l)
        self.assertEqual((wlist[0].start_point, wlist[0].end_point),
                         (datetime(2015, 1, 1, 11, 0), datetime(2015, 1, 1, 12, 00)))

        #self.start_point < co.end_point and self.end_point > co.start_point
        #happy: middle
        #def test_difference_middle(self):
        l = Section(datetime(2015, 1, 1, 9, 30), datetime(2015, 1, 1, 11, 00))  #with in worktime

        wlist = w.difference(l)
        self.assertEqual((wlist[0].start_point, wlist[0].end_point),
                         (datetime(2015, 1, 1, 8, 30), datetime(2015, 1, 1, 9, 30)))
        self.assertEqual((wlist[1].start_point, wlist[1].end_point),
                         (datetime(2015, 1, 1, 11, 00), datetime(2015, 1, 1, 12, 00)))

        #self.start_point < co.end_point and self.end_point > co.start_point
        #happy: middle
        #def test_difference_none(self):
        l = Section(datetime(2015, 1, 1, 13, 00), datetime(2015, 1, 1, 14, 00))  #cover

        wlist = w.difference(l)
        self.assertEqual((wlist[0].start_point, wlist[0].end_point),
                         (datetime(2015, 1, 1, 8, 30), datetime(2015, 1, 1, 12, 00)))


if __name__ == '__main__':
    unittest.main()

