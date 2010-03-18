# -*- coding: utf-8 -*-

# TODO:
# * Refactor parser functions into class.
# * Move classes into separate files.
# * More robust parser code.
# * Possibly read restaurant and phonenumbers from command line arguments.
# * Read parser configuration from config files.
# * Presave data for restaurants each week.
# * Keep list of phonenumbers and restaurants in db.
# * Write unit tests.
# * Setup continuous integration.
# * Add code to github.
# * Create subscription page.
# * Create subscription SMS receive function.

import urllib
import xpath
from xml.dom.minidom import parse, parseString
import re
from datetime import date
import html5lib
from html5lib import treebuilders

menuurl = "http://www.kvartersmenyn.se/start/rest/9598"
phonenumber = "0706355789"
username = "blog"
password = "EvilE"

def loadUrl(url, params=None, method="GET"):
    if params and method == "GET":
        url = url + "?%s" % params
        params = None
    f = urllib.urlopen(url, params)
    s = f.read()
    f.close()
    return s

def parseHtml():
    #f = open("menu.html")
    f = loadUrl(menuurl)
    parser = html5lib.HTMLParser(tree=treebuilders.getTreeBuilder("dom"))
    doc = parser.parse(f)
    return doc

def getMenu():
    doc = parseHtml()
    weekdays = ["Måndag", "Tisdag", "Onsdag", "Torsdag", "Fredag", "Lördag", "Söndag"]
    menu = []
    c = 2
    i = 0
    while i < 5:
        weekmenu = xpath.findvalue("//p[@align='center']/font[$day]", doc, day=c)
        c = c + 1
        if weekmenu and len(weekmenu) > 7:
            i = i + 1
            regexp = r'(' + '|'.join(weekdays) + ')$' 
            weekmenu = re.sub( regexp, '', weekmenu)
            menu.append(weekmenu)
            #print "Day " + str(i) + "\n " + weekmenu
    return menu

class SMS:
    sendurl = "http://www.mosms.com/se/sms-send.php"
    username = ""
    password = ""
    type = ""

    def __init__(self, username, password, type="text"):
        self.username = username
        self.password = password
        self.type = type

    def send(self, phonenumber, message):
        params = urllib.urlencode({
            "username": self.username,
            "password": self.password,
            "nr": phonenumber,
            "type": self.type,
            "data": message.encode("latin-1"),
        })
        result = loadUrl(self.sendurl, params, "GET")
        return result

weekday = date.today().weekday()
if weekday >= 5:
    quit()

menus = getMenu()
menu = menus[weekday]

if menu:
    mess = SMS(username, password)
    result = mess.send(phonenumber, menu)

    if result <> "0":
        print "Kunde inte skicka meddelande: " + menu
        print "Orsak: " + result
    else:
        print "Meddelande skickat:" + menu
else:
    print "Hittade ingen meny för idag."
