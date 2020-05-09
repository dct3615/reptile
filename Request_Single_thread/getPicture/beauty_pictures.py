# -*- coding: utf-8 -*-
"""
Created on 2020/5/2 20:36

@author: dct
"""
import requests
import re
import os
import time


"""请求网页"""
# url_base = 'https://www.vmgirls.com/13810.html'
url_base = 'https://www.vmgirls.com/13708.html'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36',}
response = requests.get(url_base, headers = headers)
html = response.text
# print(html)

"""解析网页"""
dir_name = re.findall('<title>(.*?)</title>',html)[-1]
print(dir_name)

urls = re.findall('<a href="(.*?)" alt=".*?" title=".*?">',html)
print(urls)

"""保存图片"""
if not os.path.exists(dir_name):
    os.mkdir(dir_name)

for url in urls:
    time.sleep(1)
    pic_name = url.split('/')[-1]
    response = requests.get(url, headers = headers)
    with open(dir_name + '/' + pic_name, 'wb') as f:
        f.write(response.content)