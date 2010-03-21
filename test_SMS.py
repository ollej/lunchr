"""
Test suite for SMS
"""

import unittest
from test import test_support
import minimock
from SMS import SMS
import lunchr

class SMSTest(unittest.TestCase):
    def setUp(self):
        lunchr.loadUrl = minimock.Mock('lunchr.loadUrl', returns='0')
        self.SMS = SMS('username', 'password', 'type')

    def tearDown(self):
        del self.SMS
        minimock.restore()

    def test_constructor(self):
        """
        Tests that SMS constructor sets values properly.
        """
        self.assertEquals('username', self.SMS.username)
        self.assertEquals('password', self.SMS.password)
        self.assertEquals('type', self.SMS.type)

    def test_send(self):
        """
        Tests that SMS.send() can send an SMS.
        """
        result = self.SMS.send('phonenumber', 'message')
        self.assertEquals('0', result)

def test_main():
    test_support.run_unittest(SMSTest)

if __name__ == '__main__':
    test_main()
