"""
Test suite for lunchr
"""

import unittest
from minimock import Mock

class LunchrTest(unittest.TestCase):
    def setUp(self):
        self.html = """
            <html><head></head><body>
            <h1>Hello World</h1>
            <p align='center'>
            <font>Day 1 - qwerty asdf</font>
            <font>Empty</font>
            <font>Day 2 - qwerty asdf</font>
            <font>Day 3 - qwerty asdf</font>
            <font>Day 4 - qwerty asdf</font>
            <font>Day 5 - qwerty asdf</font>
            </p>
            </body></html>
        """
        self.menu = [
            "Day 1 - qwerty asdf",
            "Day 2 - qwerty asdf",
            "Day 3 - qwerty asdf",
            "Day 4 - qwerty asdf",
            "Day 5 - qwerty asdf",
        ]

    def tearDown(self):
        minimock.restore()

    def test_loadUrl(self):
        """
        Tests that loadUrl can download a web page
        IOError('socket error', (-2, 'Name or service not known'))
        """
        MockResponse = Mock('ResponseObject')
        MockResponse.read.mock_returns = self.html
        urllib2.urlopen = Mock('urllib2.urlopen', returns=MockResponse)
        self.assertEquals(self.html, loadUrl('http://www.example.com'))

    def test_parseHtml(self):
        """
        Tests that parseHtml returns a proper dom tree.
        TODO: Needs to check dom tree structure somehow.
        """
        self.assertEquals(doc, parseHtml(self.html))

    def test_extractMenu(self):
        """
        Tests that extractMenu returns 5 lunch menus
        """
        doc = parseHtml(self.html)
        self.assertEquals(self.menu, extractMenu(doc))

    def test_getMenu(self):
        """
        Tests that getMenu returns the menu for given weekday 
        TODO: Check isn't actually done yet.
        """
        MockResponse = Mock('ResponseObject')
        MockResponse.read.mock_returns = self.html
        urllib2.urlopen = Mock('urllib2.urlopen', returns=MockResponse)
        self.assertEquals("Day 3 - qwerty asdf", getMenu('http://www.example.com', 3))

    def test_sendLunchMenu(self):
        """
        Tests that sendLunchMenu returns the menu for given weekday 
        TODO: Check isn't actually done yet. Needs a mock SMS object. 
        """
        SMS = Mock('SMS')
        SMS.send.mock_returns = "0"
        self.assertEquals(None, sendLunchMenu("Dummy menu"))

    def test_lunchr(self):
        """
        Tests that lunchr correctly calls getMenu() and sendLunchMenu()
        TODO: Check isn't actually done yet. Needs mock functions.
        """
        self.assertEquals(None, lunchr())

    def test_lunchr_weekend(self):
        """
        Tests that sendLunchMenu raises an exception when run on weekends.
        TODO: Check isn't done. Need to fake that it is weekend.
        """
        date.today.weekday = Mock('date.today.weekday', returns=6)
        self.assertRaises(Exception("No lunch menu on the weekend."), lunchr())


class SMSTest(unittest.TestCase):
    def setUp(self):
        pass

    def test_constructor(self):
        """
        Tests that SMS constructor sets values properly.
        TODO: Needs configuration values.
        """
        messer = SMS('username', 'password', 'type')
        self.assertEquals('username', messer.username)
        self.assertEquals('password', messer.password)
        self.assertEquals('type', messer.type)

    def test_send(self):
        """
        Tests that SMS.send() can send an SMS.
        TODO: Needs mockup for urllib, and default conf values.
        """
        loadUrl = Mock('loadUrl', returns='0')
        messer = SMS('username', 'password')
        result = messer.send('phonenumber', 'messge')
        self.assertEquals('0', result)


