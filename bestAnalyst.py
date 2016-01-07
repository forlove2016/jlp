#!/usr/bin/env python2.7.4
#coding=utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import re
import urllib2

def getHtml(url):
    page = urllib2.urlopen(url)
    html_1 = page.read()
    return html_1

html= getHtml("http://q.stock.sohu.com/jlp/res/list.up?query.bestAnalyst=true")

tr=re.compile(r'<tr[^>]*>([\s\S]*?)</tr>')
tb=re.compile(r'<td[^>]*>([\s\S]*?)</td>')
linksearch=re.compile(r'<a[^>]*>([\s\S]*?)</a>')

for row in tr.findall(html):
   m=0
   for col in tb.findall(row):
       if (m==0 or m==1 or m==2 or m==14 or m==13):
           temp=""
           for li in linksearch.findall(col):
               temp=temp+" "+ li
           col=temp
       col=col.replace('\t','').replace('\n','').decode('gbk').encode('utf8').strip()
       print col,
       m=m+1
   print

