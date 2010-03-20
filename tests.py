"""
Test suite for lunchr
"""

from django.test import TestCase

class LunchrTest(TestCase):
    def test_loadUrl(self):
        """
        Tests that loadUrl can download a web page
        TODO: Needs urllib mockup.
        """
        self.failUnlessEqual(str, loadUrl(''))

    def test_parseHtml(self):
        """
        Tests that parseHtml returns a proper dom tree.
        TODO: Needs to check dom tree structure somehow.
        """
        html = "<html><head></head><body><h1>Hello World</h1></body></html>"
        self.failUnlessEqual(str, parseHtml(html))

    def test_parseMenu(self):
        """
        Tests that parseMenu returns 5 lunch menus
        TODO: Check isn't actually done yet.
        """
        self.failUnlessEqual(str, parseMenu(doc))

class SMSTest(TestCase):
    def test_constructor(self):
        """
        Tests that SMS constructor sets values properly.
        TODO: Needs configuration values.
        """
        messer = SMS(username, password, type)
        self.failUnlessEqual(username, messer.username)
        self.failUnlessEqual(password, messer.password)
        self.failUnlessEqual(type, messer.type)

    def test_send(self):
        """
        Tests that SMS.send() can send an SMS.
        TODO: Needs mockup for urllib, and default conf values.
        """
        messer = SMS(username, password)
        result = messer.send(phonenumber, msg)
        self.failUnlessEqual('0', result)


