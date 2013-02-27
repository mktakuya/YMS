# -*- coding:utf-8 -*-
import smtplib
from pit import Pit

class Mailer:
    def __init__(self, account):
        self.account = account
        self.login = Pit.get(self.account)
        self.gmail_account = self.login["account"]
        self.passwd = self.login["passwd"]

    def createMessage(self, subject, body):
        self.to_addr = self.account
        self.cc = []
        self.bcc = []
        self.fp = open("addr_list.txt", "r")

        tmp = self.fp.readline().rstrip()
        while tmp:
            self.bcc.append(tmp)
            tmp = self.fp.readline().rstrip()
        self.to_addrs = [self.to_addr] + self.cc + self.bcc

        self.from_addr = self.account
        self.message_subject = subject
        self.message_text = body
        self.message = "From: %s\r\n" % self.from_addr + "To: %s\r\n" % self.to_addr + "CC: %s\r\n" % ",".join(self.cc) + "Subject: %s\r\n" % self.message_subject + "\r\n"  + self.message_text

    def sendMessage(self):
        self.srv = smtplib.SMTP('smtp.gmail.com', 587)
        self.srv.ehlo()
        self.srv.starttls()
        self.srv.ehlo()
        self.srv.login(self.gmail_account, self.passwd)
        self.srv.sendmail(self.from_addr, self.to_addrs, self.message.encode("cp932"))
        self.srv.close()

