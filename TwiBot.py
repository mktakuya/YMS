# -*- coding:utf-8 -*-
import twoauth
from pit import Pit

class TwiBot:
    def __init__(self, user):
        self.user = user
        login = Pit.get(self.user)
        self.ckey = login["ckey"]
        self.csecret = login["csecret"]
        self.atoken = login["atoken"]
        self.asecret = login["asecret"]

        self.api = twoauth.api(self.ckey, self.csecret, self.atoken, self.asecret)
        
    def post(self, body):
        self.body = body
        self.api.status_update(body)

