"""This file contains code for use with "Think Stats",
by Allen B. Downey, available from greenteapress.com

Copyright 2014 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html
"""

from __future__ import print_function, division

import unittest

import thinkplot
import thinkstats2


class Test(unittest.TestCase):

    def testHist(self):
        hist = thinkstats2.Hist(['red', 'green', 'blue'])
        hist['red'] += 1
        print(hist)
        thinkplot.Hist(hist, width=1)
        thinkplot.Show()


if __name__ == "__main__":
    unittest.main()
