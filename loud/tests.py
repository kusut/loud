import unittest
from loud import Loud
from nose.plugins import PluginTester


class TestLoudPerfect(PluginTester, unittest.TestCase):
    activate = '--perfect'
    plugins = [Loud()]
    args = ['~/Downloads/godlike.wav']

    def test_loud_perfect(self):
        print self.output

    def makeSuite(self):
        class TC(unittest.TestCase):
            def runTest(self):
                pass
                #raise ValueError("Perfect test failed")
        return unittest.TestSuite([TC()])


class TestLoudFail(PluginTester, unittest.TestCase):
    activate = '--fail'
    plugins = [Loud()]
    args = ['~/Downloads/fatality.wav']

    def test_loud_fail(self):
        print self.output

    def makeSuite(self):
        class TC(unittest.TestCase):
            def runTest(self):
                pass
                #raise ValueError("Fail test failed")
        return unittest.TestSuite([TC()])


result = unittest.TestResult()

case_perfect = TestLoudPerfect('test_loud_perfect')
case_fail = TestLoudFail('test_loud_fail')

case_perfect(result)
case_fail(result)
