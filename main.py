# -*- coding:utf-8 -*-
from PageComparer import PageComparer
from TwiBot import TwiBot
from Mailer import Mailer
import datetime

page = PageComparer("http://www.tomakomai-ct.ac.jp/i/urgency/index.php", "index.html")

if page.compare() == True: 
    exit()

page.sync()

if page.check() == True:
    exit()

now = datetime.datetime.now()

mailer = Mailer("yotedori@mktakuya.net")
body = now.strftime("%Y/%m/%d %H:%M:%S") + u"\n学生連絡ページの更新を検知しました。\n" + u"確認をお願いします。\n" + u"http://www.tomakomai-ct.ac.jp/i/urgency/index.php\n\n" + u"---\nYotedori Monitoring System by @mktakuya"

mailer.createMessage(u"Y-ALERT（緊急嵐闥ﾊり速報）", body)
mailer.sendMessage()

y_bot = TwiBot("yotedori_bot")
y_bot.post(body)

