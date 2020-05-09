# -*- coding: utf-8 -*-
"""
Created on 2020/1/30 15:58

@author: dct
"""
import requests
from lxml import etree


def getJokeList(baseurl='http://www.budejie.com/text/{0}'):
    #nextPage = True
    pagenum = 1
    # while nextPage:
    while pagenum <= 1:
        url=baseurl.format(pagenum)
        response = requests.get(url)
        selector=etree.HTML(response.text)

        jokes = selector.xpath('//div[@class="j-r-list-c-desc"]//a//text()')
        print(jokes)
        for joke in jokes:
            yield joke

        pagenum += 1
        # hasNext= selector.xpath('//a[@class="pagenxt"]')
        # if hasNext:
        #     pagenum += 1
        # else :
        #     nextPage = False


if __name__=='__main__':
    f=open('basejie.txt','w', encoding="utf-8")
    Jokelist = getJokeList()
    for joke in Jokelist:
        f.writelines(joke)
        f.writelines('\r\n')
        f.writelines('~'*100)
        f.writelines('\r\n')
    f.close()
