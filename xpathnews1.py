# -*- coding: utf-8 -*-
"""
Created on Thu Sep 15 09:41:10 2016

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

    filename = 'xpathnews1' + '.html'
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

r = requests.get('http://indiatoday.intoday.in/')
html = r.content
root = lxml.html.fromstring(html)

urls = root.xpath('//div[@class="top_menu"]//@href')
for url in urls:
    if str(url).find('/1/')>0:
       l1.append(url)
       
for l in l1:
    r = requests.get(l)
    html = r.content
    root = lxml.html.fromstring(html)   
    urls = root.xpath('//div[@class="innerbox"]//@href')
    l2.extend(urls)
    
for l in l2:
    u = "http://indiatoday.intoday.in/"
    r = requests.get(urljoin(u,l))
    html = r.content
    root = lxml.html.fromstring(html)   
    
    title = root.xpath('//h1/text()')
    article = root.xpath('//div[@class="right-story-container"]/span/p/text()')
    title1 = u''.join(title).encode('utf-16')
    article1 = u''.join(article).encode('utf-16')
    wrapStringInHTMLWindows()
open_new_tab('xpathnews1.html')
    
    


