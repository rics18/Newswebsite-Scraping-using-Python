# -*- coding: utf-8 -*-
import lxml.html
import requests
from urlparse import urljoin
from webbrowser import open_new_tab
l1=[]
l2=[]
l3=[]

def wrapStringInHTMLWindows():
    import datetime
    now = datetime.datetime.today().strftime("%Y%m%d-%H%M%S")

    filename = 'tamilhindu' + '.html'
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
    
r = requests.get('http://tamil.thehindu.com/')
html = r.content
root = lxml.html.fromstring(html)

urls = root.xpath('//div[@id="nav-bar"]//@href')
l1.extend(urls)

for l in l1:
    r = requests.get(l)
    html = r.content
    root = lxml.html.fromstring(html)   
    urls = root.xpath('//h3[@class="grey"]//@href')
    l2.extend(urls)
l3 = urljoin(u'',l2)

for l in l3:
    r = requests.get(l)
    html = r.content
    root = lxml.html.fromstring(html)   
    
    title = root.xpath('//h1/text()')
    article = root.xpath('//div[@class="article-body"]/p/text()')
    title1 = u''.join(title).encode('utf-16')
    article1 = u''.join(article).encode('utf-16')
    wrapStringInHTMLWindows()
open_new_tab('tamilhindu.html')
    
    


