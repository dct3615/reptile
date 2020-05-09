# -*- coding: utf-8 -*-
"""
Created on 2020/5/3 8:28

@author: dct
"""

from bs4 import BeautifulSoup
import re
import requests
import sqlite3

def main():
    baseUrl = ""
    """1、爬取网页"""
    datalist = getData(baseUrl)
    savePath = ''
    saveData(savePath)
    """3、保存数据"""

def getData(baseUrl):
    datalist = []
    """2、解析数据"""
    return datalist


def saveData(savePath):
    pass

if __name__ == "__main__":
    print("start")