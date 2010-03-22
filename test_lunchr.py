"""
Test suite for lunchr
"""

import unittest
from test import test_support
import minimock
import lunchr
from SMS import *
import urllib2
from datetime import date
import xml.dom.minidom

class LunchrTest(unittest.TestCase):
    def setUp(self):
        f = open('menu.html', 'r')
        self.html = f.read()
        f.close()

        self.menu = [
            u'* # KYCKLINGFIL\xc9m. dragons\xe5s, champinjoner & ris* # \xa4 FISKm. kr\xe4ftor, dill, tomat & kokt potatis# \xa4 CHORIZO m. coleslaw & klyftpotatisVEG: QUORN m. coleslaw & klyftpotatis',
            u'STEKT FL\xc4SKm. hemlagad raggmunk & lingon# FISKGRYTAm. stj\xe4rnanis, saffran, curry & gr\xe4dde* \xa4 PASTA BOLOGNESE# VEG: B\xd6NGRYTAm. stj\xe4rnanis, curry, saffran & rotfrukter',
            u'* INDISK LAMMGRYTA m. basmatirisSTEKT STR\xd6MMINGm. brynt sm\xf6r, r\xe5r\xf6rda lingon & potatismos* # \xa4 PANNBIFF m. l\xf6ksky & stekt potatisVEG: V\xc5RRULLAR m. sweet chilidipp & ris',
            u'\xc4RTSOPPA & PANNKAKOR m. sylt & gr\xe4dde# SEJ m. \xe4gg- & persiljes\xe5s samt kokt potatis* \xa4 KYCKLINGFAJITASm. paprika, salsa & tortillas* VEG: QUORNFAJITASm. paprika, salsa & tortillas',
            u'KHALEDS PANPIZZA* \xa4 SOJABR\xc4SERAD KARR\xc9m. purjol\xf6k & jasminris# \xa4 STEKT FISKm. hummerbearnaise & kokt potatisVEG: PIZZA'
        ]

        # urllib2.urlopen mock object
        MockResponseHtml = minimock.Mock('ResponseObject')
        MockResponseHtml.read.mock_returns = self.html
        self.urlopen_mock = minimock.Mock('urllib2.urlopen', returns=MockResponseHtml)

        # SMS mock object
        SMSMock = minimock.Mock('SMSMock')
        SMSMock.send.mock_returns = '0'
        self.SMS = minimock.Mock('lunchr.SMS', returns=SMSMock)

        # Mock object for date 
        lunchr.date = minimock.Mock('lunchr.date')

    def tearDown(self):
        minimock.restore()

    def test_loadUrl(self):
        """
        Tests that loadUrl can download a web page
        IOError('socket error', (-2, 'Name or service not known'))
        """
        urllib2.urlopen = self.urlopen_mock
        self.assertEquals(self.html, lunchr.loadUrl('http://www.example.com'))

    def test_parseHtml(self):
        """
        Tests that parseHtml returns a proper dom tree.
        TODO: Needs to check dom tree structure somehow.
        """
        dom = lunchr.parseHtml(self.html)
        self.assertTrue(isinstance(dom, xml.dom.minidom.Document))

    def test_extractMenu(self):
        """
        Tests that extractMenu returns 5 lunch menus
        """
        doc = lunchr.parseHtml(self.html)
        self.assertEquals(self.menu, lunchr.extractMenu(doc))

    def test_getMenu(self):
        """
        Tests that getMenu returns the menu for given weekday 
        """
        urllib2.urlopen = self.urlopen_mock
        self.assertEquals(u'\xc4RTSOPPA & PANNKAKOR m. sylt & gr\xe4dde# SEJ m. \xe4gg- & persiljes\xe5s samt kokt potatis* \xa4 KYCKLINGFAJITASm. paprika, salsa & tortillas* VEG: QUORNFAJITASm. paprika, salsa & tortillas', lunchr.getMenu('http://www.example.com', 3))

    def test_sendLunchMenu(self):
        """
        Tests that sendLunchMenu returns the menu for given weekday 
        """
        lunchr.SMS = self.SMS
        self.assertEquals(None, lunchr.sendLunchMenu("Dummy menu"))

    def test_lunchr(self):
        """
        Tests that lunchr correctly calls getMenu() and sendLunchMenu()
        TODO: Check isn't done yet. Needs mock functions.
        """

        urllib2.urlopen = self.urlopen_mock
        lunchr.date.today.mock_returns = date(2010, 3, 18)
        lunchr.SMS = self.SMS

        self.assertEquals(None, lunchr.lunchr())

    def test_lunchr_weekend(self):
        """
        Tests that sendLunchMenu raises an exception when run on weekends.
        """

        lunchr.date.today.mock_returns = date(2010, 3, 21)

        self.assertRaises(lunchr.LunchrWeekdayException, lunchr.lunchr)

def test_main():
    test_support.run_unittest(LunchrTest)

if __name__ == '__main__':
    test_main()

