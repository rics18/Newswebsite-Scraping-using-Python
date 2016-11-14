# -*- coding: utf-8 -*-
"""
Created on Thu Sep 15 17:23:44 2016

@author: user
"""

import lxml.html
import requests
from urlparse import urljoin
from webbrowser import open_new_tab
l1=[]
l2=[]

def wrapStringInHTMLWindows():
    import datetime
    now = datetime.datetime.today().strftime("%Y%m%d-%H%M%S")

    filename = 'xpathnews2' + '.html'
    f = open(filename,'a')

    wrapper = """<html>
    <head>
    <h1>%s</h1>
    <h2>Date:%s</h2>
    </head>
    <body><p>%s</p></body>
    </html>"""

    whole = wrapper % (str(title), now, str(article))
    f.write(whole)
    f.close()

r = requests.get('http://indianexpress.com/')
html = r.content
root = lxml.html.fromstring(html)

urls = root.xpath('//*[@id="common"]/nav/ul/li/a/@href')
l1.extend(urls)
       
for l in range(1,8):
    u = "http://indianexpress.com/"
    r = requests.get(urljoin(u,l1[l]))
    html = r.content
    root = lxml.html.fromstring(html)   
    urls = root.xpath('//div[@class="caption"]//@href')
    l2.extend(urls)
    
for l in l2:
    r = requests.get(l)
    html = r.content
    root = lxml.html.fromstring(html)   
    t = root.xpath('//h1/text()')
    title = u''.join(t).encode('utf-16')
    a = root.xpath('//div[@class="articles"]//p/text()')
    article = u''.join(a).encode('utf-16')
    wrapStringInHTMLWindows()
open_new_tab('xpathnews2.html')    