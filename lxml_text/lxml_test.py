# -*- coding: utf-8 -*-
"""
Created on 2020/5/3 13:47

@author: dct
"""

from lxml import etree

def parse_text(text):
    htmlElement = etree.HTML(text)
    print(etree.tostring(htmlElement,encoding='utf-8').decode('utf-8'))

def parse_tengxun_text(text):
    htmlElement = etree.parse(text)
    print(etree.tostring(htmlElement,encoding='utf-8').decode('utf-8'))

def parse_lagou_text():
    parser = etree.HTMLParser(encoding='utf-8')
    htmlElement = etree.parse('lagou.html',parser=parser)
    print(etree.tostring(htmlElement,encoding='utf-8').decode('utf-8'))

if __name__ == '__main__':
    parse_lagou_text()
    # parse_lagou_text('lagou.html')