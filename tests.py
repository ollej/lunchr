"""
Test suite for lunchr
"""

import unittest

class LunchrTest(unittest.TestCase):
    def setUp(self):
        pass

    def test_loadUrl(self):
        """
        Tests that loadUrl can download a web page
        TODO: Needs urllib mockup.
        """
        self.assertEquals(str, loadUrl(''))

    def test_parseHtml(self):
        """
        Tests that parseHtml returns a proper dom tree.
        TODO: Needs to check dom tree structure somehow.
        """
        html = "<html><head></head><body><h1>Hello World</h1></body></html>"
        self.assertEquals(str, parseHtml(html))

    def test_extractMenu(self):
        """
        Tests that extractMenu returns 5 lunch menus
        TODO: Check isn't actually done yet.
        """
        self.assertEquals(str, parseMenu(doc))

    def test_getMenu(self):
        """
        Tests that getMenu returns the menu for given weekday 
        TODO: Check isn't actually done yet.
        """
        self.assertEquals(str, getMenu(menuurl, weekday))

    def test_sendLunchMenu(self):
        """
        Tests that sendLunchMenu returns the menu for given weekday 
        TODO: Check isn't actually done yet. Needs a mock SMS object. 
        """
        self.assertEquals(None, sendLunchMenu(menu))

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
        self.assertRaises(Exception("No lunch menu on the weekend."), lunchr())


class SMSTest(unittest.TestCase):
    def setUp(self):
        pass

    def test_constructor(self):
        """
        Tests that SMS constructor sets values properly.
        TODO: Needs configuration values.
        """
        messer = SMS(username, password, type)
        self.assertEquals(username, messer.username)
        self.assertEquals(password, messer.password)
        self.assertEquals(type, messer.type)

    def test_send(self):
        """
        Tests that SMS.send() can send an SMS.
        TODO: Needs mockup for urllib, and default conf values.
        """
        messer = SMS(username, password)
        result = messer.send(phonenumber, msg)
        self.assertEquals('0', result)


