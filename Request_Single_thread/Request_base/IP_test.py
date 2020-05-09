# -*- coding: utf-8 -*-
"""
Created on 2020/5/3 9:53

@author: dct
"""
import requests

proxy = {
    "http" : '123.57.61.38:8118'
}

response = requests.get("http://httpbin.org/ip", proxies = proxy)
print(response.text)



