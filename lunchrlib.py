# -*- coding: utf-8 -*-

import urllib2
import xpath
import re
from xml.dom.minidom import parse, parseString
from datetime import date
import html5lib
from html5lib import treebuilders

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
        raise Exception("Couldn't send message: " + menu, "The reason returned was: " + result)

def lunchr():
    weekday = date.today().weekday()
    if weekday >= 5:
        raise Exception("No lunch menu on the weekend.")

    menu = getMenu(menuurl, weekday)

    if not menu:
        raise Exception("Couldn't find a lunch menu for today.")

    sendLunchMenu(menu)
    print "Message sent:\n" + menu

