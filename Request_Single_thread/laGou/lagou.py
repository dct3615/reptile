# -*- coding: utf-8 -*-
"""
Created on 2020/5/4 10:10

@author: dct
"""
import json

import requests
from lxml import etree
import time
import os
import re

header = {'User-Agent':'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0',
          'referer': 'https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput=',
          'Cookie': 'user_trace_token=20200102111739-544c3893-cfb3-460b-a384-3afe3b7e6f93; _ga=GA1.2.1773883637.1588469447; LGUID=20200503093045-79adcab5-46b7-4f59-ac1f-6067cc15e281; _gid=GA1.2.919133323.1588469631; gate_login_token=0664e172ad4d1fccde86bd8a71ea6814ce41dcd0dbbaed4faf8ac933ccc6c0f5; LG_LOGIN_USER_ID=e07e7d6cb23bd838f523493ed590214ad6865ab7d184ed9febe48b20064f1877; LG_HAS_LOGIN=1; privacyPolicyPopup=false; index_location_city=%E5%8C%97%E4%BA%AC; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2216f6442580715f-08a1664a16a94c-67e1b3f-1049088-16f64425808821%22%2C%22%24device_id%22%3A%2216f6442580715f-08a1664a16a94c-67e1b3f-1049088-16f64425808821%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24os%22%3A%22Windows%22%2C%22%24browser%22%3A%22Chrome%22%2C%22%24browser_version%22%3A%2277.0.3865.90%22%7D%7D; _putrc=287B5A691ECD8BB2123F89F2B170EADC; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1588482603,1588487793,1588557682,1588598863; login=true; unick=%E8%91%A3%E4%BC%A0%E4%BA%AD; LGSID=20200504212742-4bf0ed09-fe34-4f58-b4a7-266ed591a23c; X_MIDDLE_TOKEN=2f1608cd454c552e142e1fad38bcf08a; X_HTTP_TOKEN=57681dcf4c50f6f92661068851ed36b9403648929b; _gat=1; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1588602323; LGRID=20200504222521-6328607f-c43b-461d-9ee9-89a998f88323',
          'accept': 'application/json, text/javascript, */*; q=0.01',
          'accept-encoding': 'gzip, deflate, br',
          'accept-language': 'zh-CN,zh;q=0.9',
          'content-length': '25',
          'origin': 'https://www.lagou.com',
          'sec-fetch-dest': 'empty',
          'sec-fetch-mode': 'cors',
          'sec-fetch-site': 'same-origin'
        }

def get_page(url, page_num):
    for i in range(1, page_num + 1):
        formdata = {'first': 'false',
                    'pn': i,
                    'kd': 'python'}
        try:
            r = requests.post(url, headers = header, data=formdata)
            time.sleep(1)
            print('链接成功')
            print(r.json().keys())
            yield r.json()
        except:
            print('链接失败')

def parse_page(pageList):
    for page in pageList:
        if page.get('content'):
            contentLists = page.get('content').get('positionResult').get('result')
            for content in contentLists:
                positionName = content.get('positionName')
                companyFullName = content.get('companyFullName')
                print(positionName,companyFullName)



url = 'https://www.lagou.com/jobs/positionAjax.json?city=%E5%8C%97%E4%BA%AC&needAddtionalResult=false'
pageList = get_page(url,10)
parse_page(pageList)