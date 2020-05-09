# -*- coding: utf-8 -*-
"""
Created on 2020/1/30 10:14

@author: dct
"""
import requests


url ="https://book.douban.com/"
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36',}
response = requests.get(url, headers = headers)
r = response.text
print(r)

