#!/usr/bin/env python2.7.4
#coding=utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import re
import urllib2
import chardet

def getHtml(url):
    page = urllib2.urlopen(url)
    html_1 = page.read()

    
    return html_1

def gettab(html):
    reg = r'<td.+/td>'
    tab = re.compile(reg)
    tablist = re.findall(tab,html)
    
    return tablist      
   
html= getHtml("http://q.stock.sohu.com/jlp/rank/hotRecomm.up")


tr=re.compile(r'<tr[^>]*>([\s\S]*?)</tr>')
td=re.compile(r'<td[^>]*>([\s\S]*?)</td>')
linksearch=re.compile(r'<a[^>]*>([\s\S]*?)</a>')

for row in tr.findall(html):
   m=0
   for col in td.findall(row):
       col=col.replace('\t','').replace('\n','').decode('gbk').encode('utf8').strip()
       if(m==1):
           for li in linksearch.findall(col):
               col=li
       if m==4:
           for li in linksearch.findall(col):
               col=li
       print col,
       m=m+1
   print

