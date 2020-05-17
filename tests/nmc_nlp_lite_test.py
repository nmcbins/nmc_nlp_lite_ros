#!/usr/bin/env python
PKG='nmc_nlp_lite'
#import roslib; roslib.load_manifest(PKG)  # This line is not needed with Catkin.

import sys
import unittest

## A sample python unit test
class dummyTest(unittest.TestCase):

    def test_one_equals_one(self):
        pass

if __name__ == '__main__':
    import rosunit
    rosunit.unitrun(PKG, 'test_bare_bones', dummyTest)