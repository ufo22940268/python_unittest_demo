__author__ = 'cc'

import unittest

device1 = None


def initDevice1():
    print "init device android"
    global device1;
    device1 = "Android"


class BaseTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        if not device1:
            initDevice1()

        cls.device1 = device1
