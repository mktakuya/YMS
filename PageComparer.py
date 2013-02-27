# -*- coding:utf-8 -*-
import urllib2
from BeautifulSoup import BeautifulSoup

class PageComparer:
    def __init__(self, url, path):
        self.url = url
        self.path = path
        self.new = BeautifulSoup(urllib2.urlopen(self.url))
        self.local = open(self.path)
        self.local = BeautifulSoup(self.local.read())

    def isChanged(self):
        if self.new == self.local:
            return False

        return False if unicode(str(self.new), "utf-8").find(u"連絡事項はありません") != -1 else True

    def sync(self):
        self.fp = open("index.html", "w")
        self.fp.write(str(self.new))
        self.fp.close()

