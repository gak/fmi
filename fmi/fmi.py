#!/usr/bin/env python

__version__ = '0.0.2'

import json
import urllib
import mechanize
import cookielib

class FMI:

    def __init__(self, username, password):
        self.username = username
        self.password = password

        self.br = mechanize.Browser()
        cookies = mechanize.CookieJar()
        self.br.set_cookiejar(cookielib.LWPCookieJar())

    def login(self):
        r = self.br.open('https://auth.me.com/authenticate?service=findmyiphone&ssoNamespace=appleid&formID=loginForm&returnURL=aHR0cHM6Ly9tZS5jb20vZmluZC8=&anchor=findmyiphone&lang=en')
        f = self.br.select_form(nr=0)
        self.br.form['username'] = self.username
        self.br.form['password'] = self.password
        r = self.br.submit()
    
    def devices(self, locate=None):

        # XXX: The 'p02' bit has changed on me in the past. Need to
        # automatically detect the domain
        url = 'https://p02-fmipweb.me.com/fmipservice/client/refreshClient'

        d = {
            "serverContext": {
                "prefsUpdateTime": 1292534976281,
                "maxDeviceLoadTime": 60000,
                "authToken": None,
                "classicUser": True,
                "sessionLifespan": 900000,
                "deviceLoadStatus": 200,
                "preferredLanguage": "en-us",
                "lastSessionExtensionTime": None,
                "clientId": "Y2xpZW50XzEzMDMzNzcyMjFfMTI5MjUzNDM1MDMwMg==",
                "timezone": {"tzCurrentName":"Eastern Summer Time (New South Wales)",
                    "previousTransition": 1286035199999,
                    "previousOffset": 36000000,
                    "currentOffset": 39600000,
                    "tzName": "Australia/Sydney"
                },
                "callbackIntervalInMS": 10000,
                "validRegion": True,
                "maxLocatingTime": 90000,
                "hasDevices": True,
                "prsId": 1303377221,
                "id": "server_ctx"
            },
            "clientContext": {
                "appName":"MobileMe Find (Web)",
                "appVersion": "1.0",
            }
        }

        if locate:
            d['clientContext']['shouldLocate'] = True
            d['clientContext']['selectedDevice'] = locate

        data = json.dumps(d, separators=(',', ':'))

        r = self.br.open(url, data)
        response = r.read()
        return json.loads(response)

