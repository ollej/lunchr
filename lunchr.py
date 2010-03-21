# -*- coding: utf-8 -*-

import urllib2
import xpath
import re
from xml.dom.minidom import parse, parseString
from datetime import date
import html5lib
from html5lib import treebuilders
from SMS import *

# Configuration
menuurl = "http://www.kvartersmenyn.se/start/rest/9598"
menuurl = "file:///Users/olle/Documents/Development/python/lunchr/menu.html"
phonenumber = ""
username = ""
password = ""

class LunchrException(Exception):
    "Default lunchr exception."

class LunchrParseException(LunchrException):
    "lunchr parse exception."

class LunchrWeekdayException(LunchrException):
    "lunchr date exception."

def loadUrl(url, params=None, method="GET"):
    if params and method == "GET":
        url = url + "?%s" % params
        params = None
    f = urllib2.urlopen(url, params)
    s = f.read()
    f.close()
    return s

def parseHtml(html):
    parser = html5lib.HTMLParser(tree=treebuilders.getTreeBuilder("dom"))
    doc = parser.parse(html)
    return doc

def extractMenu(doc):
    weekdays = ["Måndag", "Tisdag", "Onsdag", "Torsdag", "Fredag", "Lördag", "Söndag"]
    menu = []
    c = 2
    i = 0
    menudoc = xpath.find("//div[@class='menyn']", doc)
    while i < 5 and c < 20:
        #weekmenu = xpath.findvalue("//p[@align='center']/font[$day]", menudoc[0], day=c)
        weekmenu = xpath.findvalue("//font[$day]", menudoc[0], day=c)
        c = c + 1
        if weekmenu and len(weekmenu) > 7:
            i = i + 1
            regexp = r'(' + '|'.join(weekdays) + ')$' 
            weekmenu = re.sub(regexp, '', weekmenu)
            menu.append(weekmenu)
            #print "Day " + str(i) + "\n " + weekmenu
        #else:
            #print "Found no weekmenu"

    if c == 20:
        raise LunchrParseException("Couldn't find any lunch menu.")

    return menu

def getMenu(menuurl, weekday):
    html = loadUrl(menuurl)
    doc = parseHtml(html)
    menus = extractMenu(doc)
    menu = menus[weekday]
    return menu

def sendLunchMenu(menu):
    mess = SMS(username, password)
    result = mess.send(phonenumber, menu)

    if result <> "0":
        raise LunchrException("Couldn't send message: " + menu, "The reason returned was: " + result)

def lunchr():
    weekday = date.today().weekday()
    if weekday >= 5:
        raise LunchrWeekdayException("No lunch menu on the weekend.")

    menu = getMenu(menuurl, weekday)

    if not menu:
        raise LunchrException("Couldn't find a lunch menu for today.")

    sendLunchMenu(menu)
    print "Message sent:\n" + menu

# Call the main function.
if __name__ == '__main__':
    lunchr()

