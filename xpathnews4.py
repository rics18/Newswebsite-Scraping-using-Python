# -*- coding: utf-8 -*-
"""
Created on Wed Oct 12 10:36:06 2016

@author: user
"""

import lxml.html
import requests
from webbrowser import open_new_tab
l1=[]
l2=[]
l3=[]

def wrapStringInHTMLWindows():
    import datetime
    now = datetime.datetime.today().strftime("%Y%m%d-%H%M%S")

    filename = 'xpathnews4' + '.html'
    f = open(filename,'a')

    wrapper = """<html>
    <head>
    <h1>%s</h1>
    <h2>Date:%s</h2>
    </head>
    <body><p>%s</p></body>
    </html>"""

    whole = wrapper % (str(title1), now, str(article1))
    f.write(whole)
    f.close()
    
r = requests.get('http://www.thehindu.com/')
html = r.content
root = lxml.html.fromstring(html)

urls = root.xpath('//*[@id="nav-bar"]/li/a/@href')
l1.extend(urls)

for l in range(3,8):
    r = requests.get(l1[l])
    html = r.content
    root = lxml.html.fromstring(html)   
    urls = root.xpath('//div[@class="section-columns"]//h3//@href')
    l2.extend(urls)

for l in l2:
    r = requests.get(l)
    html = r.content
    root = lxml.html.fromstring(html)   
    
    title = root.xpath('//h1/text()')
    article = root.xpath('//*[@id="article-block"]/div/p/text()')
    title1 = u''.join(title).encode('utf-16')
    article1 = u''.join(article).encode('utf-16')
    wrapStringInHTMLWindows()
open_new_tab('xpathnews4.html')