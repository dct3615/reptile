# -*- coding: utf-8 -*-
"""
Created on 2020/1/30 10:01

@author: dct
"""
import requests
from lxml import etree

def getNewsURLList(baseURL):
    x = requests.get(baseURL)
    x.encoding = 'utf-8'
    selector = etree.HTML(x.text)
    contents = selector.xpath('//div[@id = "content_right"]/div[@class = "content_list"]/ul/li[div]')
    for eachlink in contents:
        url = eachlink.xpath('div[@class = "dd_bt"]/a/@href')[0]
        if url[:4] != 'http': # 有些网页地址只写了后边的一部分
            url = 'http://www.chinanews.com' + url
        label = eachlink.xpath('div/a/text()')[0]
        title = eachlink.xpath('div[@class = "dd_bt"]/a/text()')[0]
        ptime = eachlink.xpath('div[@class = "dd_time"]/text()')[0]
        yield(label, title, url, ptime)

def getNewsContent(urllist):
    for label, title, url, ptime in urllist:
        x = requests.get(url)
        x.encoding = 'utf-8'
        selector = etree.HTML(x.text)
        contents = selector.xpath('//div[@class="left_zw"]/p/text()')
        news = '\r\n'.join(contents)
        yield label, title, url, ptime, news

if __name__ == '__main__':
    urltemplate = 'http://www.chinanews.com/scroll-news/{0}/{1}{2}/news.shtml'
    testurl = urltemplate.format('2020','01','30')
    print(testurl)
    urllist = getNewsURLList(testurl)
    # for row in urllist:
    #     print(row)
    newscontents = getNewsContent(urllist)
    f = open('news.txt', 'w', encoding="utf-8")
    w = lambda x: f.write(x + u'\r\n')
    for label, title, url, ptime, news in newscontents:
        w(u'~' * 100)
        w(label)
        w(title)
        w(url)
        w(ptime)
        w(news)
    f.close()