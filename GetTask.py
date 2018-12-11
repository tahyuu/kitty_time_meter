#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
author: Yong Tan
"""

import sys
from PyQt4 import QtGui,QtCore,Qt
import time
import datetime
import codecs
import os
from bs4 import BeautifulSoup
import re
import cookielib
import urllib
import urllib2
import cookielib
import random
import json


try:
    import configparser 
    from urllib import request
    from urllib.request import urlopen
except:
    import urllib as request
    import ConfigParser as configparser 
try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s:s


def bs4_paraser(html):
    all_value = []
    value = {}
    soup = BeautifulSoup(html, 'html.parser')
    all_div = soup.find_all('div', attrs={'class': 'message-other sign_message'})
    #print all_div
    for row in all_div:
        teacher=''
        msg=''
        all_div_teacher = row.find_all('div', attrs={'class': 'main'},limit=1)
        if all_div_teacher:
            teacher=all_div_teacher[0].h1.string
            if teacher==u'二（4）班(杨丽)':
                print u'数学',
                pass
            elif teacher==u'二（4）班(陈红)':
                print u'英语',
                pass
            elif teacher==u'二（4）班(唐佳媛)':
                print u'语文',
                pass
            #print all_div_teacher[0].h1.string
       
        all_div_date = row.find_all('div', attrs={'class': 'bottom'},limit=1)
        if all_div_date:
            print all_div_date[0].span.string
            pass

        all_div_msg = row.find_all('div', attrs={'class': 'content'},limit=1)
      
	#print all_div_msg[0].span
        if all_div_msg:
            if all_div_msg[0].span:
                pre=re.compile('>(.*?)<')
                #msg = str(all_div_msg[0].span)
                #print type(all_div_msg[0].span)
                msg=''.join(pre.findall(str(all_div_msg[0].span).decode('utf-8')))
                #msg=all_div_msg[0].span.string
		#print msg
            elif all_div_msg[0].dd:
                msg=all_div_msg[0].dd.string
            if msg:
                pass
                #print msg,
        #msg=str(msg)
        #print msg,type(msg)
        #msg=msg.decode('utf-8')
        #print msg
        if msg:
            #print msg
            #msg=msg.replace(' ','')
            msg=re.sub(u"([\.\、\～]+)(\d+)",r'--\2',msg)
            msg=msg.replace(' ','')
            #msg=re.sub(u"(\d{1}\、|\d{1}\.)",r'  \1',msg)
            msg=re.sub(u"(\d{1})[\、\.]",r'  \1,',msg)
            #msg=msg.replace(' ','')
            #match_obj=re.match(u"[1-5]{1}[\、|\.][\u4e00-\u9fa5|\w|\d|\、|\：|\（\|）|\，|\《|\》|\-|\.|\—]+",msg) 
            #msg=msg.decode('utf-8')
            p=re.compile(u"\d+[\、\.\,][\u4e00-\u9fa5|\w|\d|\、|\：|\（|\）|\，|\《|\》|\-|\.|\—]+")
            list_t = p.findall(msg)
            if list_t:
                for t in list_t:
                    print "-----%s" %t.encode('utf-8')
            else:
                #print msg.encode('utf-8')
                msg=re.sub(u"通知\s*\·",'',msg)
                msg=re.sub(u"数学\s*\：",' 1,',msg)
                #print msg.count(u"该消息暂不支持，请到手机客户端进行查看")
                if msg.count(u"该消息暂不支持，请到手机客户端进行查看")<=0:
                    print "-----%s" %msg.encode('utf-8')
            #match_obj=re.match(u"\d+",msg.decode('utf-8')) 
            #if match_obj:
            #    print match_obj.group()
        
            
        #print
def GetTask():
        filename = 'cookie.txt'
        cookie = cookielib.MozillaCookieJar(filename)
        opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
        #login
        loginUrl= 'https://www.xiaoheiban.cn//NewUser-login?username=18321631629&password=rain20110621&autologin=true'
        buff= opener.open(loginUrl)
        loginstatus= buff.read()
        if  eval(loginstatus)["status"]==200:
            msgUrl= 'https://www.xiaoheiban.cn/Message'
            buff= opener.open(msgUrl)
            #data = f.read().decode('utf-8')
            msg = buff.read().decode('utf-8')
            bs4_paraser(msg)

def replacement(m):
    p_str=m.group()
    return p_str.replace()


if __name__=="__main__":
    GetTask()


