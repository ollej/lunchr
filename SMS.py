# -*- coding: utf-8 -*-

import urllib
import lunchr

class SMS:
    sendurl = "http://www.mosms.com/se/sms-send.php"
    username = ""
    password = ""
    type = ""

    def __init__(self, username, password, type="text"):
        self.username = username
        self.password = password
        self.type     = type

    def send(self, phonenumber, message):
        params = urllib.urlencode({
            "username": self.username,
            "password": self.password,
            "nr":       phonenumber,
            "type":     self.type,
            "data":     message.encode("latin-1"),
        })
        result = lunchr.loadUrl(self.sendurl, params, "GET")
        return result

