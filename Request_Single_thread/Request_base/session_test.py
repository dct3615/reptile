# -*- coding: utf-8 -*-
"""
Created on 2020/5/3 10:12

@author: dct
"""
import requests

# response = requests.get('https://www.baidu.com')
# """获取cookie"""
# print(response.cookies.get_dict()) # 百度传给的cookie

session = requests.Session()
